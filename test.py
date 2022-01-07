n=int(input()); lst=[]; sum=0
for i in range(n):
    k=int(input())
    if k==0: lst.pop()
    else: lst.append(k)
for i in lst:
    sum+=i
print(sum)
        
'''
t=int(input())
for _ in range(t):
    s=0; k=int(input()); n=int(input())
    for ki in range(k):
        if ki == 1: s += n*(n+1)/2
        elif ki == 2: s += n*(n+1)*(2n+1)
    print(s)
'''