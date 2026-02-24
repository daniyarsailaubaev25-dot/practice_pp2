def sq(a, b):
    for i in range(a, b+1):
        yield i**2
        
a, b = map(int, input().split())
res = []
for j in sq(a, b):
    res.append(j)
    
print(*res)