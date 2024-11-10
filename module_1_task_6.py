my_dict = {'Oleg': 2001, 'Dima': 1999, 'Kate': 2003}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Oleg'))
print('Not existing value:',my_dict.get('Miha'))
my_dict.update({'Gena': 1987,
                'Nina': 1990})
a = my_dict.pop('Oleg')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
print()
my_set = {1, 2, 'string', 18, 5, 3, 1, 'string'}
print('Set:', my_set)
my_set.update({99, 88})
my_set.discard(1)
print('Modified set:', my_set)
