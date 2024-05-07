grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_ = sorted(list(students))
count = 0
for i in grades:
    grades[count] = sum(i) / len(i)
    count += 1
dict_ = dict(zip(students_, grades))
print(dict_)
