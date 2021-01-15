
def insertion_sort(arr, size):

    for i in range(1, size):
        value = arr[i]
        j = i - 1
        """ this loop compares each element to its previous element and if the previous element is greater 
            than the element it moves the unsorted sub array by one element towards right and inserts the current 
            element """
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = value

    print(arr)


x = [6, 2, 9, 4, 1]
length_of_the_list = len(x)
insertion_sort(x, length_of_the_list)
