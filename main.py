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

if __name__ == "__main__":
    # Searching Algorithm
    # Binary Search
    arr_even = [2, 4, 65, 86, 102, 200]
    x_arr_even = 4
    answer_arr_even = 102
    arr_odd = [54, 124, 678, 700, 765, 993]
    x_arr_odd = 0
    answer_arr_odd = 54
    arr_single = [4]
    x_arr_single = 0
    answer_arr_single = 4

    if (binary_search(arr_even, 0, (len(arr_even)-1), answer_arr_even) == x_arr_even):
        print("arr_even answer correct!")
    else:
        print("arr_even answer incorrect!")

    if (binary_search(arr_odd, 0, (len(arr_odd)-1), answer_arr_odd) == x_arr_odd):
        print("arr_odd answer correct!")
    else:
        print("arr_odd answer incorrect!")

    if (binary_search(arr_single, 0, (len(arr_single)-1), answer_arr_single) == x_arr_single):
        print("arr_single answer correct!")
    else:
        print("arr_single answer incorrect!")