
def canconstruct(thisstring, strarray) -> bool:
    if thisstring == "":
        return True
    
    for i in strarray:
        #check if the main string has the substring as its prefix
        if thisstring.startswith(i):
            suffix = thisstring[len(i):]
            res = canconstruct(suffix, strarray)
            if res == True:
                return True
    return False



print(canconstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(canconstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
