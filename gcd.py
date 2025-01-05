'''
Greatest Common Divisor
gcd(a, b) = gcd(b, a mod b)
gcd(a, 0) = a
'''

def gcd(a, b):
    while b > 0:
        t = a % b
        a = b
        b = t 
    return a

def gcdrs(a, b):
    if b == 0:
        return a
    return gcdrs(b, a % b)

print(gcdrs(45,24))
print(gcd(45, 24))
