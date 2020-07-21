# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Your code here
    # Grab two values from list a and b with a counter from for loop
    # if one is less than other append to end of list, while other can go to current list location
    # for i in range(0, len(arrB), 2):
    #     if arrA[i] < arrB[i]:
    #         merged_arr[i] = arrA[i]
    #         merged_arr[i + 1] = arrB[i]
    #     elif arrB[i] < arrA[i]:
    #         merged_arr[i] = arrB[i]
    #         merged_arr[i + 1] = arrA[i]

    # return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    # if len(list) is 0, then return list

    # use len(list) to find lowest, middle, and highest
    # partition into list of 1
    # compare neighbors and merge
    # lowest = 0
    # highest = len(arr)
    # middle = (lowest + highest) // 2

    # left = arr[lowest: middle]
    # right = arr[middle: highest]

    # if len(left) != 1 and len(right) != 1:
    #     print(left)
    #     print(right)
    #     return merge_sort(left) + merge_sort(right)
    # elif len(left) == 1 and len(right) == 1:
    #     print(left)
    #     print(right)
    #     return merge(left, right)

    # return arr

    # STRETCH: implement the recursive logic for merge sort in a way that doesn't
    # utilize any extra memory
    # In other words, your implementation should not allocate any additional lists
    # or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    pass
    # Your code here


def merge_sort_in_place(arr, l, r):
    pass
    # Your code here
