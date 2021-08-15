def bubble_sort(list, length):
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


x = [6, 2, 9, 4, 1]
length_of_the_list = len(x)
bubble_sort(x, length_of_the_list)
print(x)
