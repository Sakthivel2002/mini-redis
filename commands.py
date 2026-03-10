from store import Store

store = Store(max_keys=3)


def execute(command_string):
    parts = command_string.strip().split()

    if not parts:
        return "ERROR"

    cmd = parts[0].upper()

    try:

        if cmd == "SET":
            key = parts[1]
            value = parts[2]

            ttl = None

            if len(parts) == 5 and parts[3].upper() == "EX":
                ttl = int(parts[4])

            return store.set(key, value, ttl)

        elif cmd == "GET":
            key = parts[1]
            value = store.get(key)

            return value if value else "(nil)"

        elif cmd == "DEL":
            key = parts[1]
            return store.delete(key)

        elif cmd == "TTL":
            key = parts[1]
            return store.ttl(key)

        else:
            return "UNKNOWN COMMAND"

    except Exception:
        return "ERROR"