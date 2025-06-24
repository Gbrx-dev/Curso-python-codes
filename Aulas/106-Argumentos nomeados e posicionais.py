"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y):
    print(f'{x=} y={y}', '|' 'x + y =', x + y)

soma(10, 20)
soma(y=10, x=20)
