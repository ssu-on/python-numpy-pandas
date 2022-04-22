#4344
import numpy as np

number = int(input())
for i in range(number):
    num = list(map(int, input().split()))
    arr = np.array(num[1:])
    avg = arr.mean()
    avg_arr = np.full(num[0],avg)
    arr_result = arr>avg_arr
    count = 0
    for i in range(num[0]):
        if(arr_result[i]==True):
            count+=1
    print('%.3f' %(count/num[0]*100)+'%')
