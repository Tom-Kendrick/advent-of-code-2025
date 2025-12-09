with open("input.txt", "r") as f:
    data = f.read()
    batteries = data.split("\n")

def part_two(batteries):
    total = 0
    for battery in batteries:
        remove = len(battery) - 12
        stack = []
        for digit in battery:
            while stack and remove > 0 and stack[-1] < digit:
                stack.pop()
                remove -= 1
            stack.append(digit)
        if remove > 0:
            stack = stack[:-remove]
        max_battery = ''.join(stack)
        max_val = int(max_battery)
        total += max_val
        #print(f"Max value for battery {battery}: {max_val}")
    return total
    
def part_one(batteries):
    total = 0
    for battery in batteries:
        max_val = -1
        for i in range(len(battery) - 1):
            tens = int(battery[i])
            remaining_digits = battery[i+1:]
            ones = int(max(remaining_digits))

            current_val = (tens * 10) + ones
        
            if current_val > max_val:
                max_val = current_val
        total += max_val
        #print(f"Max value for battery {battery}: {max_val}")
    return total

print("Part One:", part_one(batteries))
print("Part Two:", part_two(batteries))
        