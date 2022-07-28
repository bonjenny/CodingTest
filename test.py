n=int(input())

def hanoi(fr, to, ex, num):
    if num==1: print(fr, to); return
    hanoi(fr, ex, to, num-1)
    print(fr, to)
    hanoi(ex, to, fr, num-1)

print(2**n-1)
hanoi(1, 3, 2, n)
