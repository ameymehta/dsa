rows = 5
columns = 6

grid1 = [[0 for c in range(columns)] for r in range(rows)]

row = [0] * columns
grid2 = [row] * rows

print('grid1')
for r in range(rows):
    print(grid1[r])

print('grid2')
for r in range(rows):
    print(grid2[r])