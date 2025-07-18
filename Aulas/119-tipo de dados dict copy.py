# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list

pessoa = {
    'nome': 'Gabriel',
    'sobrenome': 'Santos',
    'idade': 23,
    'altura': 1.8,
    'endereços': [
        {'rua': 'Rua X', 'número': 543},
        {'rua': 'Rua Y', 'número': 987},
    ],
}

print(pessoa['endereços'])
print(pessoa['nome'])
print()

for chave in pessoa:
    print(chave, pessoa[chave])