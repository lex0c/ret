def run_command(command):
    import subprocess

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

    if result.returncode == 0:
        print(result.stdout)
    else:
        print(result.stderr)

run_command("!!COMMAND!!")
