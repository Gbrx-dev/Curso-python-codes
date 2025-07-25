#  Empacotamento e desempacotamento de dicionários

a, b = 1, 2
a, b = b, a
# print(a,b)


# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome':'Alice',
    'sobrenome': 'Souza',

}

dados_pessoa = {
    'idade': 26,
    'altura': 1.9,
}

pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)

# args e kwargs
# args 
# kwargs - keyword arguments

def mostro_argumentos_nomeaods(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeaods(1, 2, nome='Jose', sla= 123)
# mostro_argumentos_nomeaods(**pessoa_completa)

config = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeaods(**config)