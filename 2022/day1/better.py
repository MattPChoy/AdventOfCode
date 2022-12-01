"""
From xbarnett
"""

"""
Given an input (string from input text file), return an iterable containing 
the sum of each elf.

Works by passing a list of lists of integers 
    - Outermost list delimited by \n\n
    - Innermost list delimited by \n
    - Then use the map function to apply the int() function to each element 
        of the innermost list.
"""
def sums(inp):
    return [sum(map(int, i.split("\n"))) for i in inp.strip().split("\n\n")]

def solve1(inp):
    return max(sums(inp))

def solve2(inp):
    return sum(sorted(sums(inp))[-3:])

with open("input.txt", "r") as f:
    inp = f.read()
    print(solve1(inp))
    print(solve2(inp))