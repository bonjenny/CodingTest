import sys
n=int(sys.stdin.readline())
l=[int(sys.stdin.readline()) for _ in range(n)]
l.sort()
print(round(sum(l)/n))
print(l[n//2])

d=dict()
for i in set(l):
    d[i]=l.count(i)
max=[0]
for i in set(l):
    if d[i]>d[max[0]]:
        max=[i]
    elif d[i]==d[max[0]]:
        max.append(i)
try: print(max[1])
except: print(max[0])

print(l[-1]-l[0])