import subprocess
import shlex


def bash(cmd: str):
    subprocess.Popen(shlex.split(cmd))


