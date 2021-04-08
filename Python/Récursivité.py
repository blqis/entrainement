def facto_it(n):
    f = 1
    for i in range(1,n+1):
        f=f*1
    return f

def facto_rec(n):
    if n <= 0:
        return 1
    return n*facto_rec(n-1)

def fibo_it(n):
    a = 1
    b = 1
    for i in range(n-2):
        c = a + b
        a = b
        b = c
    return c



def fibo_rec(n):
    if n <= 1 or n<= 2:
        return 1
    return fibo_rec(n-1) + fibo_rec(+n-2)


def fibo_rec2(n):
    if n <= 1 or n<= 2:
        return 1
    return fibo_rec2(n)


def exp_it(x,n):
    e = 1
    for i in range(n):
        e = x*e
    return e


def exp_rec(x,n):
    if n == 0:
        return 1
    return exp_rec(x, n-1)*x

print(exp_rec(5,5))

def PGCD(a,b):
    if b%a == 0:
        return a
    return PGCD(b%a,a)

print(PGCD(56,42))



