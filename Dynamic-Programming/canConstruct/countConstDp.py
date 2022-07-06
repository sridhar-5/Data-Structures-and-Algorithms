
def canconstruct(thisstring, strarray, mem) -> int:
    if thisstring == "":
        return 1
    if thisstring in mem:
        return mem[thisstring]
    
    count = 0

    for i in strarray:
        #check if the main string has the substring as its prefix
        if thisstring.startswith(i):
            suffix = thisstring[len(i):]
            res = canconstruct(suffix, strarray,mem)
            
            count += res

    mem[thisstring] = count        
    return mem[thisstring]
   
        
mem = {}
print(canconstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], mem))
print(canconstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"], mem))
print(canconstruct("purple", ["purp", "p", "ur", "le", "purpl"], mem))

