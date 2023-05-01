import socket
import threading
import io
import sys
import struct


def execute_code(code, conn):
    try:
        output = io.StringIO()
        sys.stdout = output
        exec(code)
        sys.stdout = sys.__stdout__
        output_str = output.getvalue()
        conn.sendall(output_str.encode('utf-8'))
    except Exception as e:
        conn.sendall(str(e).encode('utf-8'))


def recv_exactly(conn, num_bytes):
    received_data = b''

    while len(received_data) < num_bytes:
        chunk = conn.recv(num_bytes - len(received_data))

        if not chunk:
            break

        received_data += chunk

    return received_data


def recv_data(conn):
    data_length_bytes = recv_exactly(conn, 4)

    if len(data_length_bytes) < 4:
        return None

    data_length = struct.unpack("!I", data_length_bytes)[0]
    data = recv_exactly(conn, data_length)

    return data.decode('utf-8')


def handle_client(conn, addr):
    with conn:
        while True:
            code = recv_data(conn)

            if not code:
                break

            code_thread = threading.Thread(target=execute_code, args=(code, conn))
            code_thread.start()


def main():
    port = 12345

    with open('./hosts', 'r') as file:
        for line in file:
            host = line.rstrip()

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
