n = int(input())
count = 0
l = []
for i in range(n):
    m = list(map(int, input().split()))
    l.append(m)
for i in l:
    sum = i.count(1)
    if sum > 1:
        count += 1
    
        
print(count)            
