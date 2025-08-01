# Isinstace - para saber se o objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Gabriel'},
]

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(4)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item.upper())
    
    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 6)
    else:
        print('OUTRO')
        print(item)