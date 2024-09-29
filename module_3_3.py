def print_params(a=1, b='Строка', c=True):  # 1
    print(a, b, c)


values_list = [2, True, 'строка']  # 2
values_dict = {'a': 5, 'b': 'СтрокA', 'c': True}  # 2
values_list_2 = [54.32, 'СТРОКА']  # 3

print_params()  # 1
print_params(b=25)  # 1
print_params(c=[1, 2, 3])  # 1
print_params(*values_list)  # 2
print_params(**values_dict)  # 2
print_params(*values_list_2, 42)  # 3
