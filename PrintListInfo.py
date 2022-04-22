import numpy as np

number = []

while True :
    print("Enter numbers. (To finish press 'Enter' key)")
    n = input()
    if len(n) == 0 :
        break
    number.append(float(n))

list = np.array(number)
list.sort()
number_len = len(list)
number_center = int(number_len/2)

print("You enetered")
print(list)

if number_len % 2 == 0 :
    median = (number[number_center - 1] + number[number_center])/2
else : median = number[number_center]

sum = list.sum()
average = np.mean(list)

print("sum : %.2f"%sum)
print("median : %.2f"%median)
print("average : %.2f"%average)
print("min : %.2f"%np.min(list))
print("max : %.2f"%np.max(list))
