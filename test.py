from pybash import bash

a = 1

print(bash("ls -l"))
print(bash("ls inexistant_file"))