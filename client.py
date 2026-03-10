import socket

HOST = "127.0.0.1"
PORT = 6380


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    print("Connected to Mini Redis. Type commands.")

    while True:
        command = input(">> ")

        if command.lower() == "exit":
            break

        client.send((command + "\n").encode())

        response = client.recv(1024).decode()

        print(response.strip())

    client.close()


if __name__ == "__main__":
    start_client()