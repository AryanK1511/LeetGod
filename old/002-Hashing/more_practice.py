# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

def equal_pairs(grid):
    d_row = {}
    d_col = {}
    for row in grid:
        if tuple(row) not in d_row:
            d_row[tuple(row)] = 1
        else:
            d_row[tuple(row)] += 1
    
    for col in range(len(grid)):
        curr_col = []
        for row in range(len(grid)):
            curr_col.append(grid[row][col])
        if tuple(curr_col) not in d_col:
            d_col[tuple(curr_col)] = 1
        else:
            d_col[tuple(curr_col)] += 1

    ans = 0
    for entry in d_row:
        if entry in d_col:
            ans += d_row[entry] * d_col[entry]
    return ans

grid = [[3,2,1],[1,7,6],[2,7,7]]
grid = [[13,13],[13,13]]

print(equal_pairs(grid))
print("==============")