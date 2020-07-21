# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Your code here
    # set pointer_a to zero
    # set pointer_b to zero
    pointer_a, pointer_b = 0, 0

    # for i length of merged_arr loop
    for i in range(len(merged_arr)):
        # check if pointer_a == length of arrA
        if pointer_a == len(arrA):
            # then overide and set merged_arr[i] to arrB[pointer_b]
            merged_arr[i] = arrB[pointer_b]
            # add one to pointer_b
            pointer_b += 1
        # check if pointer_b == length of arrB
        elif pointer_a == len(arrB):
            # then overide and set merged_arr[i] to arrA[pointer_a]
            merged_arr[i] = arrA[pointer_a]
            # add one to pointer_a
            pointer_a += 1
        # check if arrA[pointer_a] > arrB[pointer_b]
        elif arrA[pointer_a] > arrB[pointer_b]:
            # then overide and set merged_arr[i] to arrB[pointer_b]
            merged_arr[i] = arrB[pointer_b]
            # add one to pointer_b
            pointer_b += 1
        # check if arrA[pointer_a] < arrB[pointer_b]
        elif arrA[pointer_a] < arrB[pointer_b]:
            # then overide and set merged_arr[i] to arrA[pointer_a]
            merged_arr[i] = arrA[pointer_a]
            # add one to pointer_a
            pointer_a += 1

    return merged_arr


# test1 = merge([1, 3], [2, 4])
# print(test1)

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    print(arr)
    # Your code here
    # set lowest to zero
    lowest = 0
    # set highest to len of arr -1
    highest = len(arr)
    # check if length of arr is > 1

    if len(arr) > 2:
        # then middle is lowest + highest // 2
        middle = (lowest + highest) // 2
        # return merge(merge_sort(arr[:middle]) + merge_sort(arr[middle:]))
        return merge_sort(arr[:middle]) + merge_sort(arr[middle:])
    # check if length of arr == 2
    elif len(arr) == 2:
        # then return merge(array one and array two)
        split = arr.pop()
        return merge(arr, [split])

    return arr


test2 = merge_sort([1, 4, 2, 5, 3, 6])
print(test2)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input

# def merge_in_place(arr, start, mid, end):
#     pass
# Your code here

# def merge_sort_in_place(arr, l, r):
#     pass
# Your code here
