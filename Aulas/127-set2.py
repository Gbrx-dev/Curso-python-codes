# Métodos úteis:
# add, update, clear, discard

# s1 = set()
# s1.add('Gabriek')
# s1.add(1)
# s1.update(('Teste', 1, 2 , 3, 4))
# # s1.clear()
# s1.discard('Teste')
# s1.discard('Gabriek')
# print(s1)


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s1 ^ s2


print(s3)



