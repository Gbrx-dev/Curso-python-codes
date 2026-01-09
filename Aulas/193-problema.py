# Problema dos parâmetros mutáveis em funções Python
def add_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = add_clientes('Luiz')
add_clientes('Joao', cliente1)
add_clientes('Fernando', cliente1)
cliente1.append('Gab')

cliente2 = add_clientes('Helena')
add_clientes('Mario', cliente2)

cliente3 = add_clientes('Pereira')
add_clientes('Clara', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)