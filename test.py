n,k=map(int,input().split());
l=[i for i in range(1,n+1)]
d=[]; cd=k
for _ in range(n):
    if len(l)>1: c=cd-1
    else: c=0
    print('c:',c)
    d.append(l[c])
    l.remove(l[c])
    print(l)
    c+=k
    if c!=len(l) and len(l)>1: c%=len(l)
    cd=c
print('<',end='')
for i in d:
    print(i,end='')
    if i!=d[len(d)-1]: print(',',end=' ')
print('>',end='')