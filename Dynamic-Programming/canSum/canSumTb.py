def canSum(targetSum, numbers):
    dptable = [False]*(targetSum+len(numbers))

    dptable[0] = True

    for i in range(targetSum+1):
        if dptable[i] is True :
            for j in numbers:
                if (i + j ) < len(dptable):
                    dptable[i+j] = True
        
    return dptable[targetSum]


print(canSum(7,[2,3]))
print(canSum(7,[5,3,4,7]))
print(canSum(7,[2,4]))
print(canSum(8,[2,3,5]))
