import re

hand = open('docs/regex_sum_1793310.txt')
numlist = list()

for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) == 0: continue
    for num in stuff:
        numlist.append(int(num))

print(sum(numlist))