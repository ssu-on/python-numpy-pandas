#10870
array = []
array.append(0)
array.append(1)
index = 2

num = int(input())
for i in range(num-1):
    array.append(array[index-2]+array[index-1])
    index += 1
print(array[num])
