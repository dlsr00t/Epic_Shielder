###codigo para transformar bytes em string

import subprocess as sp

variavel = sp.run(['dir'], shell=True, capture_output=True)
variavel = variavel.stdout
variavel = "".join(map(chr, variavel))
print(f'\033[32m{variavel}\033[m')


