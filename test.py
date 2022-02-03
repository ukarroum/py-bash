from pybash import bash

a = "toto"

print(bash("ls -l"))
print(bash("ls inexistant_file"))

print(bash("ls -l > $toto"))

print(a)

print(toto)