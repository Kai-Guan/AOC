total = 0
for line in open("1_input.txt", "r").readlines():
    total += 10*int([i for i in line if i.isdigit()][0]) + int([i for i in reversed(line) if i.isdigit()][0])
print(total)