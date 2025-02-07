n = int(input())
s = str(input())

d = s.count("D")
a = s.count("A")
if a > d:
    print("Anton")
elif a < d:
    print("Danik")    
else:
    print("Friendship")    
