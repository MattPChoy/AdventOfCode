"""
Revised version of the code that I wrote
"""

# Read in the text file and save that as a list of strings
with open("input.txt", "r") as infile:
    lines = infile.readlines()

idx = 0 # Current index we've processed
max = -1 # Value of "best so far" (largest)
max_idx = -1 # Index of the "best so far"
calories = {0:0} # Map of index to total # of calories

# For each line in the textfile
for line in lines:
    if line == "\n":
        # Update best so far before incrementing
        if calories[idx] > max:
            max = calories[idx]
            max_idx = idx

        # New reindeer, increase the index
        idx += 1
        calories[idx] = 0
    else:
        calories[idx] += int(line)

print(max)