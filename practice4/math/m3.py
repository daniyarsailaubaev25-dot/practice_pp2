from math import tan, pi

def Area(n, s):
    return (n*pow(s, 2))/(4*tan(pi/n))
    
n,s = map(int, input().split())
print(Area(n,s))
