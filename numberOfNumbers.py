#2577
import numpy as np

arr = np.zeros(10)
print(arr)
a = int(input())
b = int(input())
c = int(input())
d = a*b*c
n = len(str(d))
num = list(str(d))
print(d)

for i in num:
    for j in range(10):
        if(int(i)==j):
            arr[j]+=1
            print(arr)

for i in range(10):
    print(arr[i])
