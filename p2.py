appearances = 0
simScore = 0
score = 0
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
    for j in range(len(row2)):
        if row2[j] == row1[i]:
            appearances = appearances + 1

    score = row1[i] * appearances
    simScore = simScore + score
    appearances = 0

print(simScore)
