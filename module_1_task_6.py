my_dict = {'Oleg': 2001, 'Dima': 1999, 'Kate': 2003}
print(my_dict)
print(my_dict.get('Oleg'))
print(my_dict.get('Miha'))
my_dict.update({'Gena': 1987,
                'Nina': 1990})
print(my_dict)
del my_dict ['Oleg']
print(my_dict)


my_set = {1, 2, 'string', 18, 5, 3, 1, 'string'}
print(my_set)
my_set.update({99, 88})
print(my_set)
print(my_set.discard(1))
print(my_set)

