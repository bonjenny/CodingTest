n=int(input())

il=[]
for _ in range(n):
    il.append(int(input()))

#과정리스트에 넣을 리스트
nl=[i for i in range(1,n+1)]
nn=0
rl=[] #결과 +- 넣을 리스트

#과정리스트
l=[]
#x만큼 +
for i in range(1, il[0]+1):
    l.append(nl[nn]);nl[nn]=0;nn+=1
    rl.append('+')
l.pop();rl.append('-')

try:
    for i in range(1, n):
        
        # 4->3 등 pop해야하는 경우
        if il[i]==il[i-1]-1:
            l.pop();rl.append('-')
        
        # 6등 6 나오기 전까지 push해야하는 경우
        elif il[i]>il[i-1]:
            for j in range(nl[nn], il[i]+1):
                l.append(nl[nn]);nl[nn]=0;nn+=1
                rl.append('+')
            l.pop();rl.append('-')
        
        # 8까지 모든 수를 다 넣은 뒤 pop해야하는 경우
        elif nl.count(0)==n:
            l.pop();rl.append('-')
        
        #예외처리
        else: print('NO'); rl=[]; break
except: print('NO')

#결과리스트 출력
else:
    for i in rl:
        print(i)
