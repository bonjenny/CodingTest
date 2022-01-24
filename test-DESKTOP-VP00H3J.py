n=int(input())
nl=[int(i) for i in input().split()]
m=int(input())
ml=[int(i) for i in input().split()]
for mi in ml:
    c=0
    for ni in nl:
        if mi==ni: print(1); c=1; break
    if c==0: print(0)