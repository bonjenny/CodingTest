while True:
    ip=input()
    if ip=='.': break
    if ip.count('[')==ip.count(']') and \
        ip.count('(')==ip.count(')'):
        ip=list(ip)
        try:
            if ip.index('[')<=ip.index(']') and \
                ip.index('(')<=ip.index(')'):
                print('yes')
            else: print('no')
        except:
            if ip.count('[')==0 and ip.count('(')!=0:
                if ip.index('(')<=ip.index(')'):
                    print('yes')
                else: print('no')
            elif ip.count('(')==0 and ip.count('[')!=0:
                if ip.index('[')<=ip.index(']'):
                    print('yes')
                else: print('no')
            else: print('yes')
    else: print('no')
