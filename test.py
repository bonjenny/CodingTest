num=int(input());
for n in range(1,num+1):
    l=[]; sum=n; i=n
    while i!=0:
        l.append(i%10);
        i//=10
    for i in range(len(l)): sum+=l[i]
    if num==1: c=0
    elif sum==num:
        c=1; print(n); break
if c==0: print(0)