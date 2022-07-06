
def canconstruct(thisstring, strarray, mem) -> bool:
    if thisstring == "":
        return True
    if thisstring in mem:
        return mem[thisstring]
    
    for i in strarray:
        #check if the main string has the substring as its prefix
        if thisstring.startswith(i):
            suffix = thisstring[len(i):]
            res = canconstruct(suffix, strarray,mem)
            if res == True:
                mem[thisstring] = True
                return mem[thisstring]

    mem[thisstring] = False
    return False

        




mem = {}
print(canconstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], mem))
print(canconstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"], mem))
