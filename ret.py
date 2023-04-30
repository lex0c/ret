import socket
import threading
import io
import sys


def execute_code(code, conn):
    try:
        output = io.StringIO()
        sys.stdout = output
        exec(code)
        sys.stdout = sys.__stdout__
        output_str = output.getvalue()
        conn.sendall(output_str.encode('utf-8'))
    except Exception as e:
        conn.sendall(e.encode('utf-8'))


def handle_client(conn, addr):
    with conn:
        while True:
            data = conn.recv(1024)

            if not data:
                break

            code = data.decode('utf-8')

            code_thread = threading.Thread(target=execute_code, args=(code, conn))
            code_thread.start()


def main():
    port = 12345

    with open('./hosts', 'r') as file:
        for line in file:
            host = line.rstrip()
            print(host)

            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
                    server_socket.bind((host, port))
                    server_socket.listen(1)

                    while True:
                        conn, addr = server_socket.accept()
                        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
                        client_thread.start()
            except:
                pass


if __name__ == "__main__":
    main_thread = threading.Thread(target=main)
    main_thread.start()

