# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

class Pessoa:
    ...

p1 = Pessoa('Gabriel', 'Santos')
p1 = nome = 'Gabriel'
p1.sobrenome = 'Santos'

p2 = Pessoa('Maria', 'Jose')
p2 = nome = 'Maria'
p2.sobrenome = 'Jose'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)