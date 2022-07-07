def haveSum(targetSum, numbers):

    dptable = [None]*(targetSum+1)
    dptable[0] = []

    for i in range(targetSum+1):
        if dptable[i] != None:
            for j in numbers:
                if i+j < len(dptable):
                    dptable[i+j] = dptable[i] + [j]
    
    return dptable[targetSum]

print(haveSum(7,[2,3]))
print(haveSum(7,[5,3,4,7]))
print(haveSum(7,[2,4]))
print(haveSum(8,[2,3,5]))
