n=int(input())
ans=0
if n//3619>0:
    print('n은 1_000_000 이상')
    ans+=n//3619*1_000_000
    n%=3619
if n//280>0:
    print('n은 100_000 이상')
    ans+=n//280*100_000
    n%=280
if n//19>0:
    print('n은 10_000 이상')
    ans+=n//19*10_000
    n%=19
print(ans)