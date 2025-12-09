import re

pattern = re.compile(r"^(\d+)\1+$")

total_sum = 0

with open("input.txt", "r") as f:
    data = f.read().strip()
    clean_data = data.replace("\n", "")
    ranges = clean_data.split(",")

for r in ranges:
    if "-" not in r: continue
    
    start_s, end_s = r.split("-")
    start = int(start_s)
    end = int(end_s)

    for num in range(start, end + 1):
        s_num = str(num)
        
        if pattern.match(s_num):

            total_sum += num

print(f"Total Sum: {total_sum}")