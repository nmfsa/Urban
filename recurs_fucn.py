def test(*params):
    print(*params)


def fact_func(n):
    if n == 1:
        return 1
    else:
        return n * fact_func(n - 1)


test(6 , "TEXT" , 8)
print(f'ِФакториал от "{5}" = {fact_func(5)}')