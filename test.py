from collections import deque
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    l=deque([[int(i),0] for i in input().split()])
    for i in range(len(l)):
        l[i][1]=i
    cnt=0
    while True:
        max=0
        for i in range(len(l)):
            if l[i][0]>max: max=l[i][0]
        if l[0][0]<max: l.rotate(-1)
        else:
            cnt+=1
            if l[0][1]==m: break
            l.popleft()
    print(cnt)