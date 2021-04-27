from math import sqrt

def getPrime(n):
    if not n%2:
        return 2
    for i in range(3,int(sqrt(n))+1,2):
        if not n%i: 
            return i
    return n

def solve(n):
    c = 0
    s = sum(map(int,str(n)))  
    while n!=1:
        p = getPrime(n)
        while not n%p:
            c+=sum(map(int,str(p)))
            n = n//p
        
    return 1 if c == s else 0

n = int(input())
print(solve(n))
