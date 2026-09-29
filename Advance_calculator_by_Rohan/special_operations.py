#Specials Operations#
def power(x,y):
    return(x**y)

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def gcd(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

def lcm(a,b):
    return (a*b)//gcd(a,b)