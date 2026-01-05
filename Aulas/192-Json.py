import json

# pessoa = {
#     'nome': 'Henrique',
#     'sobrenome': 'Santos',
#     'enderecos': [
#         {'rua':'R1','numero':45},
#         {'rua':'R2','numero': 11},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (1, 5, 6, 0, 20),
#     'dev': True,
#     'nada': None,
# }

# with open('192-json.json', 'w') as arquivo:
#     json.dump(pessoa, arquivo, indent=2)

with open('192-json.json', 'r', encoding='utf8') as arquivo:
    pessoa =json.load(arquivo)
    print(pessoa)
