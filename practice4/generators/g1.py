def Square(nums):
    for x in nums:
        yield x*x
        
N = int(input())
res = []

for j in Square(N):
    res.append(j)

print(*res)
