import sys
n=int(input())
#n=int(sys.stdin.readline())
l=[]
while n>0:
    l.append(n%10)
    n=n//10
l.sort(reverse=True)
for i in l:
    print(i,end='')