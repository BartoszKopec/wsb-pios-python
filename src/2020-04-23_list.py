import random

matrix=[]
rows=list(range(5))
columns=list(range(10))
for x in rows:
    row=''
    matrix.append([])
    for y in columns:
        matrix[x].append(random.randint(0, 10))
        row = row + ' ' + str(matrix[x][y])
    print(row)

print()
number = random.randint(0, 10)
numberCounts=0
for x in rows:
    for y in columns:
        numberCounts = matrix[x].count(number)
print('Count of',number,':', numberCounts)