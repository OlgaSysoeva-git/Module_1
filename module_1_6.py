# словари
my_dict = {'Ivan':2015,'Mariya':2018,'Aleksey':1979}
print(my_dict)
print(my_dict['Mariya'])
print(my_dict.get('Mamy'))
my_dict.update({'Valya':1978,
                'Juliya':1980})
a = my_dict.pop('Aleksey')
print(a)
print(my_dict)

# множества
my_set = {6,8,6,7,8,9,'pig','goat','pig',(10,11,12)}
print(set(my_set))
my_set.add(1)
my_set.add('elephant')
my_set.discard('goat')
print(my_set)










