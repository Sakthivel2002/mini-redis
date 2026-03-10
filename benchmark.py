import socket
import time

HOST = "127.0.0.1"
PORT = 6380
REQUESTS = 10000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

start = time.time()

for i in range(REQUESTS):
    cmd = f"SET key{i} value{i}\n"
    client.send(cmd.encode())
    client.recv(1024)

end = time.time()

elapsed = end - start

print(f"Requests: {REQUESTS}")
print(f"Time: {elapsed:.2f} seconds")
print(f"Throughput: {REQUESTS/elapsed:.2f} ops/sec")

client.close()