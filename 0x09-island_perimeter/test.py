def island_perimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    hor = []
    ver = [0] * cols
    
    for i in range(rows):
        hor_c = 0
        for j in range(cols):
            if grid[i][j] == 1:
                ver[j] += 1
                if j < cols - 1 and grid[i][j+1] == 1:
                    hor_c += 1
            else:
                if hor_c != 0:
                    hor.append(hor_c + 1)
                    hor_c = 0
        
        if hor_c != 0:
            hor.append(hor_c + 1)
    
    if len(hor) == 0:
        return 2 * sum(ver)
    
    if len(hor) == 1:
        return 2 * (hor[0] + sum(ver))
    
    return 2 * (max(hor) + max(ver))
