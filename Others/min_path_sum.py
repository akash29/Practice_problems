grid = [[1,3,1],[1,5,1],[4,2,1]]

def min_sum():
    print(grid)
    for i,j in enumerate(grid):
        for k, _ in enumerate(j):
            if i==0 and k!=0:
                grid[i][k]+=grid[i][k-1]
            if i!=0 and k==0:
                grid[i][k]+=grid[i-1][k]
            if i!=0 and k!=0:
                grid[i][k]+=min(grid[i][k-1],grid[i-1][k])


    return grid[-1][-1]

val = min_sum()
print(val)