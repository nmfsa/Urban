class Buiding:

    total = 0

    def __init__(self):
        Buiding.total += 1


a = 'a'
for i in range(1, 41):
    a = Buiding()
    print(f'Объект № {i}: {a}')
print(Buiding.total)
