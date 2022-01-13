n=int(input()); l=[2,7]
if n==1: print(2)
elif n==2: print(7)
elif n>2:
    for i in range(2,n):
        l.append(2*l[i-2]+3*l[i-1])
    print(l[n-1]%1000000007)