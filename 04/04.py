with open("input.txt", "r") as f:
    data = f.read()
    input_data = data.split("\n")
directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

def part_one(input_data, directions=directions):
    
    total = 0
    for i in range(len(input_data)):
        for j in range(len(input_data[0])):
            if input_data[i][j] == ".":
                continue
            count = 0
            for dy, dx in directions:
                nr, nc = i + dy, j + dx
                if 0 <= nr < len(input_data) and 0 <= nc < len(input_data[0]):
                    if input_data[nr][nc] == '@':
                        count += 1
            if count < 4:
                total += 1

    return total

def part_two(input_data, directions=directions):
    current_grid = [row[:] for row in input_data]
    total = 0
    while True:
        next_grid = [list(row) for row in current_grid]
        changes = 0
        for i in range(len(current_grid)):
            for j in range(len(current_grid[0])):
                if current_grid[i][j] == ".":
                    continue
                count = 0
                for dy, dx in directions:
                    nr, nc = i + dy, j + dx
                    if 0 <= nr < len(current_grid) and 0 <= nc < len(current_grid[0]):
                        if current_grid[nr][nc] == '@':
                            count += 1
                if count < 4:
                    next_grid[i][j] = '.'
                    changes += 1
        total += changes
        current_grid = next_grid
        if changes == 0:
            break

    return total


print("Part One:", part_one(input_data))
print("Part Two:", part_two(input_data))