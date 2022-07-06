def bestSum(targetSum, array, mem):
    if targetSum < 0:
        return None
    if targetSum == 0:
        return []

    shortestcombination = None
    thiscom = []
    for i in array:
        combination = bestSum(targetSum - i , array, mem)
        if combination is not None:
            thiscom = combination + [i]
            if shortestcombination is None or (len(thiscom) < len(shortestcombination)):
                shortestcombination = thiscom
    
    mem[targetSum] = shortestcombination
    return mem[targetSum]

mem = {}
print(bestSum(7,[5,3,4,7], mem ) );
print(bestSum(8, [5,4,7],mem) );
print(bestSum(7,[2,4], mem ));
print(bestSum(8, [3,5,2], mem));