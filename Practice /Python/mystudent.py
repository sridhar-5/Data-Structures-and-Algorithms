def findMissing(N, stringOfRolls):
    missingStatus = "All Present"
    x = stringOfRolls.split(" ")
    for i in range(0, len(x)):
        x[i] = int(x[i])

    use_for_comparision = []
    for i in range(N):
        use_for_comparision.append(i + 1)

    difference = []
    difference = list(set(use_for_comparision) - set(x))

    if len(difference) == 0 :
        missingStatus = "All Present"
    else:
        missingStatus = difference[0]
    return missingStatus

N = int(input())
stringOfRolls = input()
missingRoll = findMissing(N, stringOfRolls)
print(missingRoll)
