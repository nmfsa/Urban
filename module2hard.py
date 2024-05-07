print('введите число (3 - 20):')
num = int(input())
result = []
for i in range(1, num):
    for j in range(i+1, num):
        if num % (i+j) == 0:
            result.append(i)
            result.append(j)
print(*result, sep='')




