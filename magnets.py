n = int(input())  # Number of magnets

cnt = 1  # Initial count of groups
curr = input()[1]  # Read the first magnet and get the second character

for _ in range(1, n):
    compare = input()[1]  # Read the next magnet and get the second character
    if curr != compare:
        cnt += 1
        curr = compare  # Update the current character

print(cnt)
