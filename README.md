# Remote Execution Tool (RET)

The RET allows you to execute Python code remotely on a server. It consists of two parts: a server that accepts and executes the code, and a client that sends the code to the server. The server runs the code in a separate thread and sends the output back to the client.

## Usage

Install deps:
```sh
pip install -r requirements.txt
```

Start the server by running the `ret.py` script:
```sh
python ret.py
```

Run the client script with the required arguments:
```sh
python client.py --host <host> --port <port> --module <module_file_path>
```
- `--host`: The host address of the RET server
- `--port`: The port number of the RET server
- `--module`: The path to the module file to be executed remotely

The client script reads the content of the specified module file, sends it to the server, and then prints the output returned by the server.

### RET

The server script `ret.py` listens for incoming connections and creates a new thread for each client. Each thread receives the code from the client, executes it in a separate thread, and sends the output back to the client.

**ps**: The hosts file replaces a DGA algorithm.

