my_dict = {'Kseniya':1995, 'Boris':1994}
print(my_dict)
print(my_dict['Kseniya'])
print(my_dict.get('Daria', 'Такого ключа нет'))
my_dict.update ({'Lena':2020, 'Kira':2015})
print(my_dict.pop('Boris'))
print(my_dict)

my_set = {12, 'Apple', 24.025, 12, 'Apple', 24.025}
print(my_set)
my_set.update ({True, 'String'})
my_set.discard(12)
print(my_set)
