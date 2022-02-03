import sys
num=int(input())
l=[]; c=[0]*8001
for _ in range(num):
    n=int(input())
    l.append(n)
    c[n+4000]+=1
l.sort()
print(round(sum(l)/num))
print(l[num//2])

most=max(c)
cnt=0
if c.count(most) == 1:
    print(c.index(most)-4000)
else:
    for i in c:
        if i == most:
            cnt += 1
            if cnt == 1:
                c[c.index(i)] = 0
            elif cnt == 2:
                print(c.index(i)-4000)
                break
print(l[-1]-l[0])