def P(x):
    for i in range(2,x):
        if x%i==0: return False
    return True
mi,mx=map(int,input().split()); count=0
for i in range(2,int(mx**0.5)+1):
    if P(i): count+=1
print(count)
    
'''
mi,mx=map(int,input().split()); l=[]
for z in range(2,int(mx**0.5)+1):
    for i in range(1,int(mx/z**2)+1):
        if mi<=i and i<=mx:
            l.append(z**2*i)
l=sorted(list(set(l)))
print(mx-mi+1-len(l))
'''