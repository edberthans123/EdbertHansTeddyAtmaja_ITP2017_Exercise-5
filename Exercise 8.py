import math
def a(p):
    return p**2

a=lambda p:p**2
print(a(1))

def b(y, l):
    return math.sqrt(y**2 + l**2)

b=lambda y, l : y**2+l**2
print(b(1,2))

def c(*args):
    return sum(args)/len(args)

c=lambda*args:sum(args)/len(args)
print(c(9,9,0))

def d(abcd):
    return 'bcda'

d=lambda s:''.join(set(s))
print(d('happy'))

