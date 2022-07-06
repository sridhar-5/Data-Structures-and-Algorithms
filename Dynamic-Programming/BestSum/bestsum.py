def bestSum(targetSum, array):
    if targetSum < 0:
        return None
    if targetSum == 0:
        return []

    shortestcombination = None
    thiscom = []
    for i in array:
        combination = bestSum(targetSum - i , array)
        if combination is not None:
            thiscom = combination + [i]
            if shortestcombination is None or (len(thiscom) < len(shortestcombination)):
                shortestcombination = thiscom
    
    return shortestcombination

print(bestSum(7,[5,3,4,7]));
print(bestSum(8, [5,4,7]));
print(bestSum(7,[2,4]));
print(bestSum(8, [3,5,2]));