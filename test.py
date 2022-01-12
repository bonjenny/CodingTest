n,m=map(int,input().split());mm=0
lst=list(map(int,input().split()))
lst.sort(reverse=True)
print(lst)
for i in range(n):
    if m>=lst[i] and lst[i]>mm: mm=lst[i]
    print(lst[i])
    for li in range(1,len(lst)):
        if i<li:
            print(lst[i],lst[li])