import re

result = 0
with open("problem3.txt") as f:
    file = f.read()
    matching_memory = re.findall(r"mul\(\d+,\d+\)", file)
    for memory in matching_memory:
        memory = memory.strip("mul()")
        memory = memory.split(",")
        result += int(memory[0]) * int(memory[1])

print(result)