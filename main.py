import os
import sys
import time
import termcolor
import subprocess
import webbrowser


def openServer(port : int):
    print(f"[+] Starting server on port {port}...\n")

    webbrowser.open(f"http://localhost:{port}")
    subprocess.run(['python3', '-m', 'http.server', str(port)])


if len(sys.argv) > 1:
    try:
        port = sys.argv[1]
        if int(port) >= 45259 or int(port) <= 0:
            port = 8000
    except ValueError:
        errorText = f"[/!\] '{sys.argv[1]}' is not a valid port number, operation cancelled\n"
        errorTextColored = termcolor.colored(errorText, 'red')
        print(errorTextColored)
        exit()
    
    if len(sys.argv) >= 3:
        if os.path.exists(sys.argv[2]):
            startDirectory = sys.argv[2]
        else:
            errorText = f"[/!\] Path '{sys.argv[2]}' does not exist, operation cancelled\n"
            errorTextColored = termcolor.colored(errorText, 'red')
            print(errorTextColored)
            exit()
            #startDirectory = os.environ['HOME']
    else:
        startDirectory = os.environ['HOME']
else:
    port = 8000


print(f"[+] Changing directory to '{startDirectory}'")
os.chdir(startDirectory)


try:
    openServer(port)
except KeyboardInterrupt:
    print("\n[+] Closing server...\n")
    time.sleep(1)
