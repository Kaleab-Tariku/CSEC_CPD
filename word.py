s = str(input())
upper = 0
lower = 0

for i in s:
    if i.capitalize() == i:
        upper += 1
    else:
        lower += 1    
if upper <= lower:
    print(s.lower())
else:
    print(s.upper())    
