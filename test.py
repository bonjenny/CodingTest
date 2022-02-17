import sys
k,n=map(int,input().split())
#k,n=map(int,sys.stdin.readline().split())
l=[0]*k
for i in range(k):
    l[i]=int(input())
#    l[i]=int(sys.stdin.readline())

start=1
end=max(l)

while start <= end:
    mid=(start+end)//2
    value=0
    for i in range(k):
        value += (l[i]//mid)
    if value >= n:
        start = mid+1
    else:
        end = mid-1
print(end)