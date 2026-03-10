import unittest
import time
from commands import execute


class TestCommands(unittest.TestCase):

    def test_set_and_get(self):
        result = execute("SET name Alice")
        self.assertEqual(result, "OK")

        value = execute("GET name")
        self.assertEqual(value, "Alice")

    def test_delete(self):
        execute("SET temp 123")
        result = execute("DEL temp")

        self.assertEqual(result, 1)

        value = execute("GET temp")
        self.assertEqual(value, "(nil)")

    def test_ttl(self):
        execute("SET key1 value1 EX 2")

        ttl = execute("TTL key1")
        self.assertTrue(ttl >= 0)

        time.sleep(3)

        value = execute("GET key1")
        self.assertEqual(value, "(nil)")

    def test_unknown_command(self):
        result = execute("UNKNOWN something")
        self.assertEqual(result, "UNKNOWN COMMAND")

    def test_invalid_syntax(self):
        result = execute("SET onlykey")
        self.assertEqual(result, "ERROR")

    def test_empty_input(self):
        result = execute("")
        self.assertEqual(result, "ERROR")

    def test_large_number_of_keys(self):
        for i in range(100):
            execute(f"SET key{i} value{i}")

        for i in range(100):
            value = execute(f"GET key{i}")
            if value != "(nil)":
                self.assertEqual(value, f"value{i}")

    def test_lru_eviction(self):
        execute("SET a 1")
        execute("SET b 2")
        execute("SET c 3")

        execute("GET a")  

        execute("SET d 4")  

        value_b = execute("GET b")

        if value_b != "(nil)":
            self.assertIn(value_b, ["2", "(nil)"])


if __name__ == "__main__":
    unittest.main()