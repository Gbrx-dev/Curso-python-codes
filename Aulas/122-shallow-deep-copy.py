import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'li': [1, 6 , 2],
}

d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['li'][1] = 222222

print(d1)
print(d2)