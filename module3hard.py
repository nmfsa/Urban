data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
     (6, {'cube': 7, 'drum': 8}),
     "Hello",
     ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    sum = 0
    for i in args:
        for j in i:
            if isinstance(j, dict):
                for key, value in j.items():
                    sum += len(key) + value
            elif isinstance(j, int):
                sum += j
            elif isinstance(j, str):
                sum += len(j)
            else:
                 sum += calculate_structure_sum(j)
    return sum


result = calculate_structure_sum(data_structure)
print(result)


