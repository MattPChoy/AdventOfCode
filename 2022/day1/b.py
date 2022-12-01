"""
Revised version of the code that I wrote
"""

# Read in the text file and save that as a list of strings
with open("input.txt", "r") as infile:
    lines = infile.readlines()

calories = {0:0} # Map of index to total # of calories

# For each line in the textfile
for line in lines:
    if line == "\n":

        # New reindeer, increase the index
        idx += 1
        calories[idx] = 0
    else:
        calories[idx] += int(line)

inv_calories = {}
# Flip k and v in dictionary.
for k in calories:
    inv_calories[calories[k]] = k

ranked = inv_calories.keys()
ranked = [i for i in ranked]
print(type(ranked))
ranked.sort()

first = ranked[-1]
sec = ranked[-2]
thi = ranked[-3]

print(first, sec, thi)
print(first + sec + thi)