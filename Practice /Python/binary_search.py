def find_the_element(user, ele):
    right_boundary = len(user) - 1
    left_boundary = 0
    while(right_boundary >= left_boundary):
        middle_element = (left_boundary+(right_boundary-1) // 2)
        if user[middle_element] == ele:
            return middle_element
        if user[middle_element] > ele:
            right_boundary = middle_element - 1

        if user[middle_element] < ele:
            left_boundary = middle_element + 1
    return 0

user_list = []
size = int(input("please enter the size of the array : "))
for i in range(size):
    user_list.append(int(input("element :")))
element = int(input("Element to be searched : "))

a = find_the_element(user_list, element)
if a != 0:
    print("found at " + str(a))
else:
    print("not found")
