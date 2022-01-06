import math
n = int(input())
for i in range(1, n):
    print(i, ':', math.floor((math.sqrt(8*i-3)-1)/2)+1)