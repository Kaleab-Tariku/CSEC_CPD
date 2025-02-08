matrix = [list(map(int, input().split())) for i in range(5)]
store = []
center = [3, 3]
for row in matrix:
    for column in row:
        if column == 1:
            store.append(matrix.index(row) + 1)
            store.append(row.index(column) + 1)         
answer = (abs(center[0] - store[0])) + abs((center[1] - store[1]))
print(answer)
