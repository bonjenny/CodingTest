import sys
a, b = map(int, input().split())

list = input().split()
list = [int(i) for i in list]
list = map(int, sys.stdin.readline().split().rstrip())

print('{:0,.3f}%'.format(a))
