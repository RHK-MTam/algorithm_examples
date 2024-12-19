import math

# Searching Algorithm
# Binary Search
def binary_search(arr, start, end, x):
    if (start > end):
        return -1
    
    i = start + (end - start) // 2

    if (arr[i] == x):
        return i
    elif (arr[i] < x):
        return binary_search(arr, (i + 1), end, x)
    elif (arr[i] > x):
        return binary_search(arr, start, (i - 1), x)

# Exponential Search    
def exponential_search(arr, x):
    i = 0
    two = 2 ** i
    length = len(arr)
    if (length == 0):
        return -1
    if (arr[0] == x):
        return 0
 
    while (two < length and arr[two] <= x):
        i += 1
        two = 2 ** i
 
    if (two >= length):
        return binary_search(arr, (2 ** (i - 1)), (length - 1), x)
    else:
        return binary_search(arr, (2 ** (i - 1)), two, x)

# Sorting Algorithm
# Selection Sort
def selection_sort(arr):
    if (len(arr) == 0):
        return -1

    for i in range(0, (len(arr) - 1)):
        smallest_index = i
        for j in range((i + 1), len(arr)):
            if (arr[j] < arr[smallest_index]):
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    
    return arr

# Bubble Sort
def bubble_sort(arr):
    if (len(arr) == 0):
        return -1

    for i in range(0, (len(arr) - 1)):
        for j in range(0, (len(arr) - 1 - i)):
            if (arr[j] > arr[(j + 1)]):
                arr[j], arr[(j + 1)] = arr[(j + 1)], arr[j]
    
    return arr

# Insertion Sort
def insertion_sort(arr):
    if (len(arr) == 0):
        return -1
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while (key < arr[(j - 1)]):
            arr[j - 1] = arr[(j)]
            j -= 1
        arr[j] = key

    return arr

if __name__ == "__main__":
    # Searching Algorithm
    arr_even = [2, 4, 65, 86, 102, 200]
    x_arr_even = 4
    answer_arr_even = 1
    arr_odd = [54, 124, 678, 700, 765, 993]
    x_arr_odd = 993
    answer_arr_odd = 5
    arr_single = [4]
    x_arr_single = 4
    answer_arr_single = 0

    # Binary Search
    if (binary_search(arr_even, 0, (len(arr_even)-1), x_arr_even) == answer_arr_even):
        print("Binary Search: arr_even answer correct!")
    else:
        print("Binary Search: arr_even answer incorrect!")
    if (binary_search(arr_odd, 0, (len(arr_odd)-1), x_arr_odd) == answer_arr_odd):
        print("Binary Search: arr_odd answer correct!")
    else:
        print("Binary Search: arr_odd answer incorrect!")
    if (binary_search(arr_single, 0, (len(arr_single)-1), x_arr_single) == answer_arr_single):
        print("Binary Search: arr_single answer correct!")
    else:
        print("Binary Search: arr_single answer incorrect!")
    
    # Exponential Search
    if (exponential_search(arr_even, x_arr_even) == answer_arr_even):
        print("Exponential Search: arr_even answer correct!")
    else:
        print("Exponential Search: arr_even answer incorrect!")
    if (exponential_search(arr_odd, x_arr_odd) == answer_arr_odd):
        print("Exponential Search: arr_odd answer correct!")
    else:
        print("Exponential Search: arr_odd answer incorrect!")
    if (exponential_search(arr_single, x_arr_single) == answer_arr_single):
        print("Exponential Search: arr_single answer correct!")
    else:
        print("Exponential Search: arr_single answer incorrect!")

    # Sorting Algorithm
    arr_sort = [64, -25, 12, 11, 11, 0, -5]
    answer_arr_sort = [-25, -5, 0, 11, 11, 12, 64]

    # Selection Sort
    if (selection_sort(arr_sort) == answer_arr_sort):
        print("Selection Sort: arr_sort answer correct!")
    else:
        print("Selection Sort: arr_sort answer incorrect!")
    
    # Bubble Sort
    if (bubble_sort(arr_sort) == answer_arr_sort):
        print("Bubble Sort: arr_sort answer correct!")
    else:
        print("Bubble Sort: arr_sort answer incorrect!")

    # Insertion Sort
    if (insertion_sort(arr_sort) == answer_arr_sort):
        print("Insertion Sort: arr_sort answer correct!")
    else:
        print("Insertion Sort: arr_sort answer incorrect!")