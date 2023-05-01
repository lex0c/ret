import socket
import sys
import argparse
import struct


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


def send_code(code, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        encoded_code = code.encode('utf-8')

        client_socket.sendall(struct.pack("!I", len(encoded_code)))
        client_socket.sendall(encoded_code)

        resp = recv_data(client_socket)

        print(resp)


def load_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    return content


def replace_vars(content, args):
    new_content = content

    for arg in args:
        keyvalues   = arg.split("=")
        key         = keyvalues[0]
        value       = keyvalues[1]

        pattern = f"!!{key}!!"

        new_content = new_content.replace(pattern, value)

    return new_content


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True, help="Host address of the RET")
    parser.add_argument("--port", required=True, type=int, help="Port number of the RET")
    parser.add_argument("--module", required=True, help="Path to the module file")
    parser.add_argument("--values", type=str, nargs="+", help="Replace template vars")
    args = parser.parse_args()

    host    = args.host
    port    = args.port
    module  = args.module
    values  = args.values or []

    content = load_file(module)
    code = replace_vars(content, values)
    send_code(code, host, port)

