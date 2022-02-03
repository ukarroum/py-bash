import subprocess
import shlex
import re
import inspect


def bash(cmd: str) -> int:
    """
        Run a bash command provided ad a string:w

    :param cmd:
    :return: return code of the command
    """
    if re.match(r'(.*)> *\$(\w*)', cmd):
        cmd, out_var_name = re.match(r'(.*)> *\$(\w*)', cmd).groups()
    else:
        out_var_name = None

    if out_var_name:
        out = subprocess.PIPE
    else:
        out = None

    process = subprocess.Popen(shlex.split(cmd), stdout=out)

    p_out, p_err = process.communicate()

    if out_var_name:
        inspect.currentframe().f_back.f_locals[out_var_name] = p_out.decode().split("\n")

    return process.returncode
