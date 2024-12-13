import re

operation = True
result = 0

with open("problem3.txt") as f:
    file = f.read()

execute_idxs = [(m.start(0), m.end(0)) for m in re.finditer(r"d(o|on't)\(\)", file)]
memory_idxs = [(m.start(0), m.end(0)) for m in re.finditer(r"mul\(\d+,\d+\)", file)]
combined_list = execute_idxs + memory_idxs
combined_list.sort()

for item in combined_list:
    item = file[item[0]:item[1]]
    if re.match(r"do\(\)", item):
        operation = True
    elif re.match(r"mul\(\d+,\d+\)", item): 
        if operation:
            memory = item
            memory = memory.strip("mul()")
            memory = memory.split(",")
            result += int(memory[0]) * int(memory[1])
    else:
        # if its not mul or do() then its must to be don't() string
        operation = False

print(result)