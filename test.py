n=int(input())-1
ans=0
if n//3619>0:
    ans+=1_000_000*(n//3619)
    n%=3619
if n//280>0:
    if n//280 <= 6:
        ans+=100_000*(n//280)
        n%=280
    else:
        ans+=100_000*6
        n-=280*6
        if n <= 65:
            ans+=1_000*n+666
            n=-1
        elif n > 65 and n <= 1065:
            ans+=66_000+n-66
            n=-1
        elif n > 1065 and n <= 1098:
            ans+=1_000*(n-999)+666
            n=-1
        else:
            n-=1098
            ans+=1_000*(n//109)
            n%=109
if n//19>0:
    if n//19 <= 6:
        ans+=10_000*(n//19)
        n%=19
    else:
        ans+=10_000*6
        n-=19*6
        if n <= 5:
            ans+=1_000*n+666
            n=-1
        elif n > 5 and n <= 105:
            ans+=6_600+n-6
            n=-1
        elif n > 105 and n <= 108:
            ans+=1_000*(n-99)+666
            n=-1
        else:
            n-=108
            ans+=10_000*(n//19)
            n%=19
if n>=0:
    if n <= 5:
        ans+=1_000*n+666
        n=-1
    elif n > 5 and n <= 15:
        ans+=666_0+n-6
        n=-1
    elif n > 15 and n <= 18:
        ans+=1_000*(n-9)+666
        n=-1
print(ans)