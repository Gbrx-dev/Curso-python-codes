import importlib

import aula157_m

print(aula157_m.variavel)

for i in range(10):
    print(i)
    importlib.reload(aula157_m)

print('Fim')