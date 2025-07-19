# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

p1 = {
    'nome': 'Henrique',
    'sobrenome': 'Santos',
    # 'idade': 34,
}

# p1.update({
#     'nome': 'novo valor',
#     'altura': 1.8
# })

# p1.update(nome='novo valor', idade=22)

# tupla=('nome', 'novo valor'), ('idade', 20)
lista=[['nome', 'novo valor'], ['idade', 20]]
p1.update(lista)
print(p1)


# ultima = p1.popitem()
# print(ultima)
# print(p1)

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))








# pessoa.setdefault('idade', None)
# print(pessoa['idade'])
# print(len(pessoa))
# print(pessoa.keys())
# print(list(pessoa.values()))
# print(list(pessoa.items())) 