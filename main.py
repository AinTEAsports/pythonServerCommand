import os
import sys
import time
import subprocess
import webbrowser


def openServer(port : int):
    print(f"/// STARTING SERVER ON PORT {port}... ///\n")

    webbrowser.open(f"http://localhost:{port}")
    subprocess.run(['python3', '-m', 'http.server', str(port)])


if len(sys.argv) > 1:
    try:
        port = sys.argv[1]
    except ValueError:
        print(f"'{sys.argv[1]}' is not a valid port number, operation cancelled")
        exit()
    
    if len(sys.argv) >= 3:
        if os.path.exists(sys.argv[2]):
            startDirectory = sys.argv[2]
        else:
            startDirectory = os.environ['HOME']
    else:
        startDirectory = os.environ['HOME']
else:
    port = 8000


print(f"Changing directory to '{startDirectory}'")
os.chdir(startDirectory)

try:
    openServer(port)
except KeyboardInterrupt:
    print("\n/// CLOSING SERVER... ///\n")
    time.sleep(1)
