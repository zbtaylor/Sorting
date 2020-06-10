# TO-DO: complete the helper function below to merge 2 sorted arrays
# look in to .extend() method for lists


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    m = 0

    # go through both arrays while we can
    while a < len(arrA) and b < len(arrB):
        if arrA[a] <= arrB[b]:
            merged_arr[m] = arrA[a]
            a += 1
            m += 1
        else:
            merged_arr[m] = arrB[b]
            b += 1
            m += 1

    # go through array A if anything remains
    while a < len(arrA):
        merged_arr[m] = arrA[a]
        a += 1
        m += 1

    # go through array B if anything remains
    while b < len(arrB):
        merged_arr[m] = arrB[b]
        b += 1
        m += 1

    return merged_arr


def merge_sort(arr):
    # TO-DO
    # no more than 10 lines
    # recursive
    if len(arr) > 1:
        middle = round(len(arr) / 2)
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
