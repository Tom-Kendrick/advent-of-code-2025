pointer = 50
password = 0
list_length = 100

with open("input.txt", "r") as f:
    data = f.read()
    instructions = data.split("\n")

for instruction in instructions:
    if not instruction: continue
    
    steps = int(instruction[1:])
    direction = instruction[0]
    
    if direction == "R":
        password += (pointer + steps) // list_length
        pointer += steps
        
    elif direction == "L":
        password += (pointer - 1) // list_length - (pointer - steps - 1) // list_length
        pointer -= steps

    pointer = pointer % list_length

print(password)