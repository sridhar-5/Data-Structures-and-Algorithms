def find_the_element(user, ele):
    found = 0
    for i in range(len(user) - 1):
        user[i] = int(user[i])

    for i in range(len(user)-1):
        if int(user[i]) == ele:
            found = i
        else:
            found = 0
    return found


user_list = []
size = int(input("please enter the size of the array : "))
for i in range(size):
    user_list.append(input("element :"))
element = int(input("Element to be searched : "))

a = find_the_element(user_list, element)
if a != 0:
    print("found at " + str(a))
else:
    print("not found")
