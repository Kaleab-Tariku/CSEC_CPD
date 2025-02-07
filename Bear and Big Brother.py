n = list(map(int, input().split()))
is_bob_larger = False
count = 0
limak = n[0]
bob = n[1]
while limak <= bob:
    limak *=3
    bob *=2
    count += 1
    if limak > bob:
        print(count)
        is_bob_larger = True
