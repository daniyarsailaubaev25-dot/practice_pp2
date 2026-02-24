import math

def tr_area(h, a, b):
    return (a+b)/2 * h
    
h, a, b = map(int, input().split())
print(tr_area(h, a, b))