# Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(5, True, False)
print_params('Messi')
print_params(10, 23)
print_params(b=25)
print_params(c=[1, 2, 3])

# Распаковка параметров:
values_list = ['Messi', 10, True]
values_dict = {'a': '10', 'b': False, 'c': 30}
print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры:
values_list_2 = ['Ronaldo', 7]
print_params(*values_list_2, 42)
