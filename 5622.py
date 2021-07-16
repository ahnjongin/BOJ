list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
sum = 0
for j in range(len(a)):
    for i in list:
        if a[j] in i:
            sum += list.index(i) + 3

print(sum)
