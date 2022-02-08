import sys
k,n=map(int,input().split())
#k,n=map(int,sys.stdin.readline().split())
l=[0]*k
sum=0
for i in range(k):
    l[i]=int(input())
    sum+=l[i]
#    l[i]=int(sys.stdin.readline())

def bs(start, mid, end):
    if start >= end: return start
    sum=0
    mid=(start+end+1)/2
    for i in l: sum+=i//x
    if sum==n: return mid
    elif sum >= k: start=mid
    else: end=mid-1
    bs(start, mid, end)

x=sum//n
print(bs(1,(2+x)/2),x)