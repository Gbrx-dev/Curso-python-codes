import json
# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
CAMINHO_ARQUIVO = 'aula208.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 22)
p2 = Pessoa('Helena',76)
p3 = Pessoa('Maria', 15)
bd  = [vars(p1), p2.__dict__, vars(p3)]

with open (CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)