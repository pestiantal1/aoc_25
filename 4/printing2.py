neighbor_offsets = [(-1,-1), (-1,0), (-1,1),
                    (0,-1),          (0,1),
                    (1,-1),  (1,0),  (1,1)]

grid = []

def init_grid():
    with open("4_input.txt") as f:
        for line in f:
            row = []
            for char in line:
                row.append(char)
            if '\n' in row:
                row.remove('\n')
            grid.append(row)
    height = len(grid)
    width = len(grid[0])
    return grid, height, width


def solve(grid, height, width):
    cleaned = 0
    new_grid = grid

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
                    new_grid[y][x] = "."
                    cleaned += 1
    
    return new_grid, cleaned

grid, height, width = init_grid()
ans = 0
cleaned = 1

while cleaned != 0:
    grid, cleaned = solve(grid, height, width)
    ans += cleaned
    
print(ans)