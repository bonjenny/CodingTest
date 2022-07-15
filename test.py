while True:
    x=input()    
    if x=='.': break

    xl=list(x)
    x_set={'(',')','[',']'}
    xl=[i for i in xl if i in x_set]
    
    l=[]
    for i in xl:
        if i=='(' or i=='[':
            l.append(i)
        elif i==')':
            if len(l)==0: l.append(i)
            elif l[-1]=='(': l.pop()
            else: l.append(i)
        elif i==']':
            if len(l)==0: l.append(i)
            elif l[-1]=='[': l.pop()
            else: l.append(i)
    
    if len(l)==0: print('yes')
    else: print('no')
