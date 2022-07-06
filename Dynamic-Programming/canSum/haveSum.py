def haveSum(targetSum, array):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    for i in array:
        res = haveSum(targetSum - i, array)
        if res is not None:
            return res + [i]
    return None 


print(haveSum(7,[2,3]))