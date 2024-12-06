first = []
second = []
counter = 0

# get data from file
with open("problem1.txt") as f:
    for line in f:
        words = line.split("  ")
        first.append(int(words[0].strip()))
        second.append(int(words[1].strip("\n")))
    
first.sort()
second.sort()

for i in range(len(first)):
    diff = abs(first[i] - second[i])
    counter += diff

print(counter)