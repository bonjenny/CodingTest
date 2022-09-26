import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))


low = 0
high = max(l)

while True:
    h = int((low + high) / 2)
    sum = 0
    for i in l:
        temp = i - h
        if temp < 0: i = 0
        else: sum += temp

    if sum == m or low > high:
        print(h)
        break
    elif sum > m:
        low = h + 1
    else:
        high = h - 1
