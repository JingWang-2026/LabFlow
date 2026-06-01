from pathlib import Path
import socket
import subprocess
import sys


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
PORT = 8080


def is_running():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        return sock.connect_ex(("127.0.0.1", PORT)) == 0


def main():
    DATA_DIR.mkdir(exist_ok=True)
    if is_running():
        return

    python_exe = Path(sys.executable)
    if python_exe.name.lower() == "pythonw.exe":
        python_exe = python_exe.with_name("python.exe")

    stdout = (DATA_DIR / "labflow-startup.out.log").open("ab")
    stderr = (DATA_DIR / "labflow-startup.err.log").open("ab")

    subprocess.Popen(
        [str(python_exe), str(BASE_DIR / "server.py")],
        cwd=str(BASE_DIR),
        stdout=stdout,
        stderr=stderr,
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS,
        close_fds=True,
    )


if __name__ == "__main__":
    main()
