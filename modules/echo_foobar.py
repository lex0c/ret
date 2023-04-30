def shell_session():
    import subprocess
    command = 'echo "foobar";date;ls;pwd'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    print(stdout, end="")
    if stderr:
        print(stderr, end="")
shell_session()
