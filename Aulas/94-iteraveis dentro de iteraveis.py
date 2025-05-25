'''Lista de listas e seus índeces'''

salas = [
   # 0       2
   ['João', 'Maria'], #0
   # 0
   ['Elaine'], #1
   # 0       1          2
   ['Luiz', 'Gabriel', 'Eduardo'], #2
]

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
