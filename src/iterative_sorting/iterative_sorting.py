# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        bigger = arr[cur_index]
        smaller = arr[smallest_index]
        arr[smallest_index] = bigger
        arr[cur_index] = smaller

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapping = True
    while swapping:
        swapping = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                bigger = arr[i]
                smaller = arr[i + 1]
                arr[i] = smaller
                arr[i + 1] = bigger
                swapping = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
