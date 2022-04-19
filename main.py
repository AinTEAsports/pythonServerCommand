import os
import sys
import argparse
import subprocess

import termcolor
import webbrowser


def openServer(port : int):
    print(f"[+] Starting server on port {port}...\n")

    webbrowser.open(f"http://localhost:{port}")
    subprocess.run(['python3', '-m', 'http.server', str(port)])


parser = argparse.ArgumentParser(
    description='Command that permite to open a python web server'
)

parser.add_argument(
    '-p',
    '--port',
    type=int,
    nargs='?',
    default='8080',
    help='Port on which the server will run'
)

parser.add_argument(
    '-d',
    '--directory',
    type=str,
    nargs='?',
    default='./',
    help='Directory where the server will be launched'
)

args = parser.parse_args()


if not os.path.exists(args.directory):
    errorText = termcolor.colored(f"[!] The directory '{args.directory}' doesn't exists\n", 'red')
    print(errorText)
    sys.exit()
else:
    os.chdir(args.directory)


if args.port <= 0 or args.port >= 10000:
    warningText = termcolor.colored(f"[/!\\] Port '{args.port}' invalid, we switched it to 8080\n", 'yellow')
    print(warningText)
    args.port = 8080


try:
    openServer(port=args.port)
except PermissionError:
    errorText = termcolor.colored(f"\[!] The port '{args.port}' is already in use\n", 'red')
    print(errorText)
    sys.exit()
except KeyboardInterrupt:
    print("")
