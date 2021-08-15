list1 = ['(','{','[']

list2 = [')','}',']']

def balanced_para(string):
    stack_op = []
    char_array = list(string)

    for i in (char_array):
        if i in list1:
            stack_op.append(i)
        elif i in list2:
            pos = list2.index(i)
            if list1[pos] == stack_op[len(stack_op)-1]:
                stack_op.pop()
        else:
            return "NO"
    if len(stack_op) == 0:
        return "YES"
    else:
        return "NO"

testcases = int(input())
for i in range(testcases):
    string = input()
    print(balanced_para(string))


"""
{[()]}
{[(])}
{{[[(())]]}}
[{()}]{}
[({{{}}})]{
[({{{}}})]][({{{
"""

"""
{[()]}
{[(])}
{{[[(())]]}}
"""