

def get_connected_ssid_linux():
    import subprocess
    command_output = subprocess.run(["iwconfig"], capture_output=True, text=True).stdout
    return command_output.splitlines()


print(get_connected_ssid_linux())

