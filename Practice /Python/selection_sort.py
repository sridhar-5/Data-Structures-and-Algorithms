def selection_sort(list, length):
    print(length)
    for i in range(0, length):
        min = i
        for j in range(i + 1, length):
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]
    print(list)


x = [6, 2, 9, 4, 1]

length_of_the_list = len(x)

selection_sort(x, length_of_the_list)
