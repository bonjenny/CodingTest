import sys

def mat_pow(mat, n):
    if n == 0:
        return mat
    elif n == 1:
        return mat
    else:
        tmp = mat_pow(mat, n//2)
        if n % 2 == 0:
            result = mul(tmp, tmp)
        else:
            a = [1, 1, 1, 0]
            result = mul(mul(tmp, tmp), mat)
    return result


def mul(a, b):
    c = [(a[0] * b[0] + a[1] * b[2]) % 1000000007, (a[0] * b[1] + a[1] * b[3]) % 1000000007,
         (a[2] * b[0] + a[3] * b[2]) % 1000000007, (a[2] * b[1] + a[3] * b[3]) % 1000000007]
    return c


# n = int(sys.stdin.readline().strip())
n = int(input())
mat = [1, 1, 1, 0]
fibo = mat_pow(mat, n-1)
print(fibo[0])