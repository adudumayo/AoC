sumDistance = 0
row1 = []
row2 = []

with open('puzzleInput.txt', 'r') as file:
    lines = file.readlines()

    for line in lines:
        firstRower = int(line.split("   ")[0])
        secondRower = int(line.split("   ")[1])

        row1.append(firstRower)
        row2.append(secondRower)

row1.sort()
row2.sort()

for i in range(len(row1)):
    distance = abs(row1[i] - row2[i])
    sumDistance = sumDistance + distance

print(sumDistance)
