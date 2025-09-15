# map - para mapear dados
from functools import partial

def print_iter(iterator):
    print(*list(iterator), sep= '\n')
    print()


produtos = [ 
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 3', 'preco': 22.34},
    {'nome': 'Produto 1', 'preco': 14.11},
    {'nome': 'Produto 2', 'preco': 104.53},
    {'nome': 'Produto 4', 'preco': 78.90},
]

def aumentar_procentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial(aumentar_procentagem, porcentagem=1.1)

# novos_produtos = [
#     {**p, 'preco': aumentar_procentagem(p['preco'])} for p in produtos
# ]
def muda_preco_de_produtos(produto):
    return {**produto, 'preco': aumentar_dez_porcento(produto['preco'])}

novos_produtos = map(
    muda_preco_de_produtos,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)