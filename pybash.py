import subprocess
import shlex


def bash(cmd: str) -> int:
    """
        Run a bash command provided ad a string:w

    :param cmd:
    :return: return code of the command
    """
    process = subprocess.Popen(shlex.split(cmd))

    process.communicate()

    return process.returncode


