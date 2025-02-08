from collections import Counter

string = str(input())
words = []  
for i in string:
    words.append(i)
x = Counter(words)
values = list(x.values())
if len(values) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")    
    
