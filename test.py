n,m=map(int,input().split())
lst=[]; max=0; count=0

for _ in range(n): #입력받기
    lst.append(list(map(int,input().split())))

def alst(i,j,mi,mj,l):
    if j>0 and j-1!=mj: l.append([i,j-1])
    if j<m-1 and j+1!=mj: l.append([i,j+1])
    if i>0 and i-1!=mi: l.append([i-1,j])
    if i<n-1 and i+1!=mi: l.append([i+1,j])

def fmax(l):
    max=0
    for i,j in l:
        if lst[i][j]>max:
            max=lst[i][j]
    return max

for i in range(n): #max찾기
    for j in range(m):
        if lst[i][j]>max:
            max=lst[i][j]

for mi in range(n): #1. max 안에서
    for mj in range(m):
        if lst[mi][mj]==max:
            nml=[]; alst(mi,mj,mi,mj,nml) # nmax 찾기
            
            for ni,nj in nml: #2. nmax 안에서
                if lst[ni][nj]==fmax(nml):
                    nnml=[]; alst(ni,nj,mi,mj,nnml) # nnmax 찾기
                    
                    for nni,nnj in nnml: #3. nnmax 안에서
                        if lst[nni][nnj]==fmax(nnml):
                            nnnml=[]; alst(nni,nnj,ni,nj,nnnml) # nnnmax 찾기
                            
                            for nnni,nnnj in nnnml: #4. nnnmax 안에서
                                if lst[nnni][nnnj]==fmax(nnnml):
                                    sum=lst[mi][mj]+lst[ni][nj]+lst[nni][nnj]+lst[nnni][nnnj]
                                    if sum>count: count=sum
print(count)