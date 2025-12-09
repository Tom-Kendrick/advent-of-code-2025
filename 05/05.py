with open("input.txt", "r") as f:
    data = f.read()
    fresh_data = data.split("\n\n")[0].splitlines()
    ingredients = data.split("\n\n")[1].splitlines()

def part_one(fresh_data, ingredients):
    ranges = []
    total = 0
    for line in fresh_data:
        start, end = map(int, line.split('-'))
        ranges.append((start, end))
    for ingredient in ingredients:
        val = int(ingredient)
        found = False
        for start, end in ranges:
            if start <= val <= end:
                found = True
                break
        if found:
            total += 1
    return total

def part_two(fresh_data):
    total = 0
    ranges = []
    for line in fresh_data:
        start, end = map(int, line.split('-'))
        ranges.append((start, end))
    ranges.sort()
    merged = []
    current_start, current_end = ranges[0]
    for i in range(1, len(ranges)):
        next_start, next_end = ranges[i]
        if next_start <= current_end + 1:
            current_end = max(current_end, next_end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = next_start, next_end
    merged.append((current_start, current_end))
    for start, end in merged:
        total += end - start + 1
    
    return total
        

print("Part One:", part_one(fresh_data, ingredients))
print("Part Two:", part_two(fresh_data))