"""
Introdução ás funções (def) em Python
Função são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None(nada).
"""

""" def Print(a, b , c):
    print(a, b , c)

Print(1, 5 ,8) """

def saudacao(nome=''):
    print(f'Olá, {nome}!')

saudacao(input('Digite seu nome: '))