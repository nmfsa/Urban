def test(*params):
    print(*params)


def fact_func(n):
    if n == 0:
        return 1
    else:
        return n * fact_func(n - 1)


# print('Ввидите номер')
# try:
#     n = int(input())
# except ValueError:
#     print('Ошибка ввода! Ввидите номер')
#     n = int(input())

test(6 , "TEXT" , 8)
n = 5
print(f'ِФакториал от "{n}" = {fact_func(n)}')