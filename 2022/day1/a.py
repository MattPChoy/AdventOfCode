with open("input.txt", "r") as infile:
    lines = infile.readlines()

idx = 0
max = -1
max_idx = -1
calories = {0:0}

print(lines)

for line in lines:
    # print(f"Line is {line}")
    if line == "\n":
        idx += 1 # new reindeer
        calories[idx] = 0
    else:
        calories[idx] += int(line)

for i in calories:
    if calories[i] > max:
        max = calories[i]
        max_idx = i

print(max)