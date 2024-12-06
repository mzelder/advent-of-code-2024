first = []
second = []
similarity = 0

with open("problem1.txt") as f:
    for line in f:
        words = line.split("  ")
        first.append(int(words[0].strip()))
        second.append(int(words[1].strip("\n")))

    for i in first:
        counter = 0
        for j in second:
            if i == j:
                counter += 1
        
        similarity += i * counter

print(similarity)