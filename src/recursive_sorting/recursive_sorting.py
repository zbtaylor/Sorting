# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0
    m = 0
    while a < len(arrA) and b < len(arrB):
        if arrA[a] <= arrB[b]:
            merged_arr[m] = arrA[a]
            a += 1
            m += 1
        else:
            merged_arr[m] = arrB[b]
            b += 1
            m += 1

    while a < len(arrA):
        merged_arr[m] = arrA[a]
        a += 1
        m += 1

    while b < len(arrB):
        merged_arr[m] = arrB[b]
        b += 1
        m += 1

    return merged_arr


arr1 = [1, 2, 3]
arr2 = [4, 5, 6, 7]
arr3 = merge(arr1, arr2)
print(arr3)


def merge_sort(arr):
    # TO-DO

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
