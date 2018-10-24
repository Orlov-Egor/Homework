from random import randrange as rnd
n = 30
array = [rnd(100) for i in range (n)]
print(*array)
count = 0
index = 0
countX = 0
j = 1
for i in range (n):
    while j < array[i]:
        if array[i]%j==0:
            count+=1
        j+=1
    if count > countX:
        countX = count
        index = i
    count = 0
    j=1
print(index)
