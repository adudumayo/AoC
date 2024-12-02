import time

safeCount = 0
levels = []
loopBreaked = False

start_time = time.time()

def listIsAscending(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def listIsDescending(lst):
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            return False
    return True

def listIsASet(lst):
    return len(lst) == len(set(lst))

with open('puzzleInput.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    values = line.split(" ")

    for i in range(len(values)):
        levels.append(int(values[i]))

    if listIsAscending(levels) or listIsDescending(levels) and listIsASet(levels):
        print(levels)
        for i in range(len(levels)-1):
            diff = abs(levels[i] - levels[i+1])

            if (diff < 1 or diff > 3):
                loopBreaked = True
                break

        if loopBreaked:
            safeCount += 1
            loopBreaked = False

    levels = []

print(safeCount)

end_time = time.time()

elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time} seconds")
