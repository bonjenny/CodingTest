import sys
n=int(sys.stdin.readline()) # 총개수 받기

s=[]
op=[]
count = 1
temp = True

for i in range(n):
  num = int(sys.stdin.readline()) # 숫자 받기
  
  while count <= num: # s에 들어가는 숫자가 num에 도달할때까지
    s.append(count)
    op.append('+')
    count += 1

  if s[-1] == num: # 맨 끝 숫자 출력
    s.pop()
    op.append('-')
  else: temp = False # 이게 안되면
    
if temp == False: print('NO') #가짜인거고
else:
  for i in op:
    print(i)
