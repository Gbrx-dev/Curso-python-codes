# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(lista1, lista2):
    tamanho = min(len(lista1), len(lista2))
    
    resultado = []
    for i in range(tamanho):
        resultado.append((lista1[i], lista2[i]))

    return resultado

cidade= ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados= ['BA', 'SP', 'MG', 'RJ']


print(zipper(cidade, estados))