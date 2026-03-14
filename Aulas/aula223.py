# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         returno = super().upper()
#         print('DEPOIS DO UPPER')
#         return returno

# string = MinhaString('Gabriel')
# print(string.upper())

class A:
    atributo_a = 'valor a'
    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor b'
    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor c'
    def metodo(self):
        super(C, self).metodo()
        print('C')

c = C()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()