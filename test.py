from collections import deque
deq=deque()
ans=deque()
n=int(input())
for _ in range(n):
    ans.appendleft(int(input()))
print(ans)
cnt=0; inp=1
for i in range(1,len(ans)):
    print(ans[i-1])
    if ans[i]-1 != ans[i-1]:
        cnt+=1
        for j in range(ans[i]-inp):
            deq.appendleft(inp); inp+=1
            print('+', deq)
        for j in range(1,ans[i]-ans[i-1]):
            deq.popleft()
            print('-', deq)
        cnt=1
    elif ans[i]==n:
        for j in range(n-inp+1):
            deq.appendleft(inp); inp+=1
            print('+', deq)