from random import randrange as rnd
n = 70
array = [rnd(-100,100) for i in range (n)]
minum = 100
for i in range (n):
    if array[i]>0 and array[i]%2!=0 and array[i]<minum:
        minum = array[i]
print(minum)
        
