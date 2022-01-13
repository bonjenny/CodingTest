n,m=map(int,input().split())
lst=[]; max=0; count=0
for _ in range(n): #입력받기
    lst.append(list(map(int,input().split())))
def alst(i,j,mi,mj,l):
    if j>0 and j-1!=mj: l.append([i,j-1])
    if j<m-1 and j+1!=mj: l.append([i,j+1])
    if i>0 and i-1!=mi: l.append([i-1,j])
    if i<n-1 and i+1!=mi: l.append([i+1,j])
def aplst(i,j,mi,mj,nni,nnj,l):
    if j>0 and j-1!=mj and j-1!=nnj: l.append([i,j-1])
    if j<m-1 and j+1!=mj and j+1!=nnj: l.append([i,j+1])
    if i>0 and i-1!=mi and i-1!=nni: l.append([i-1,j])
    if i<n-1 and i+1!=mi and i+1!=nni: l.append([i+1,j])
def fmax(l):
    max=0
    for i,j in l:
        if lst[i][j]>max:
            max=lst[i][j]
    return max
for mi in range(n):
    for mj in range(m):
        nml=[]; alst(mi,mj,mi,mj,nml)
        for ni,nj in nml:
            if lst[ni][nj]==fmax(nml):
                nnml=[]; alst(ni,nj,mi,mj,nnml)
                for nni,nnj in nnml:
                    if lst[nni][nnj]==fmax(nnml):
                        nnnml=[]; alst(nni,nnj,ni,nj,nnnml)
                        alst(mi,mj,ni,nj,nnnml); aplst(ni,nj,mi,mj,nni,nnj,nnnml)
                        for nnni,nnnj in nnnml:
                            if lst[nnni][nnnj]==fmax(nnnml):
                                sum=lst[mi][mj]+lst[ni][nj]+lst[nni][nnj]+lst[nnni][nnnj]
                                if sum>count: count=sum
print(count)