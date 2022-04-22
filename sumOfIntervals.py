#11659
import numpy as np
n, m = map(int, input().split())
arr = list(map(int,input().split()))

for i in range(m):
    index, index2 = map(int, input().split())
    index_arr = np.array(arr[index-1:index2])
    sum = index_arr.sum()
    print(sum)
