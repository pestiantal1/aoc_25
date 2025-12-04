neighbor_offsets = [(-1,-1), (-1,0), (-1,1),
                    (0,-1),          (0,1),
                    (1,-1),  (1,0),  (1,1)]

def solve():
    x = 0
    y = 0
    grid = []
    ans = 0
    
    with open("4_input.txt") as f:
        for line in f:
            row = []
            y += 1
            for char in line:
                row.append(char)
            if '\n' in row:
                row.remove('\n')
            grid.append(row)
            x = len(row)

    height = y
    width = x

    for y in range(height):
        for x in range(width):
            if grid[y][x] == '@':
                at_count = 0
                for dy, dx in neighbor_offsets:
                    ny = y + dy
                    nx = x + dx
                    if 0 <= ny < height and 0 <= nx < width and grid[ny][nx] == '@':
                        at_count += 1
                if at_count < 4:
                    ans += 1
    
    return ans            
print(solve())