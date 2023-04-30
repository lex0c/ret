import socket, sys, argparse


def send_code(code, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(code.encode('utf-8'))

        data = client_socket.recv(1024)

        print(data.decode('utf-8'))


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


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True, help="Host address of the RET")
    parser.add_argument("--port", required=True, type=int, help="Port number of the RET")
    parser.add_argument("--module", required=True, help="Path to the module file")
    parser.add_argument("--values", type=str, nargs="+", help="Replace template vars")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    host    = args.host
    port    = args.port
    module  = args.module
    values  = args.values or []

    content = load_file(module)
    code = replace_vars(content, values)
    send_code(code, host, port)

