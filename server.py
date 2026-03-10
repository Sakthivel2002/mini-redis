import socket
import threading
import logging
from commands import execute

HOST = "127.0.0.1"
PORT = 6380

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


def handle_client(conn, addr):

    logging.info(f"Client connected: {addr}")

    while True:
        try:
            data = conn.recv(1024)

            if not data:
                break

            command = data.decode().strip()

            logging.info(f"{addr} -> {command}")

            result = execute(command)

            response = str(result) + "\n"

            conn.send(response.encode())

        except Exception as e:
            logging.error(f"Error handling client {addr}: {e}")
            break

    conn.close()
    logging.info(f"Client disconnected: {addr}")


def start_server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    logging.info(f"Mini Redis running on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()

        client_thread = threading.Thread(
            target=handle_client,
            args=(conn, addr)
        )

        client_thread.start()


if __name__ == "__main__":
    start_server()