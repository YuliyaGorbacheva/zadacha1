my_dict={'Anna': 2003, 'Max': 1990, 'Olga': 1960}   #2
print(my_dict)
print(my_dict['Max'])
my_dict['Katya']= 1999
my_dict.update({'Rose':2012, 'Vasya': 2023})
print(my_dict.pop('Anna'))
print(my_dict)

my_set={5,6,3,'a',3,'a',(1,2,3)}    #3
print(my_set)
my_set.update({8,'v'})
my_set.discard((1,2,3))
print(my_set)