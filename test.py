n=int(input()); a=1; b=1; c=0
M=1_000_000
P=M/10*5

for _ in range(2, int(n%P)):
    c=a+b; a=b; b=c

if n==1: print(1)
elif n==2: print(1)
else: print(c%M)
