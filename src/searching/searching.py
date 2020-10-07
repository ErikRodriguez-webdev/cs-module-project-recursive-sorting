# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # find middle value from list
    middle = (start + end) // 2

    if len(arr) == 0:
        return -1

    if target == arr[middle]:
        return middle
    # if target > middle value then call function again with new start and end values
    elif target > arr[middle]:
        new_start = middle + 1
        return binary_search(arr, target, new_start, end)
    # if target < middle value then call function again with new start and end values
    elif target < arr[middle]:
        new_end = middle - 1
        return binary_search(arr, target, start, new_end)

    # STRETCH: implement an order-agnostic binary search
    # This version of binary search should correctly find
    # the target regardless of whether the input array is
    # sorted in ascending order or in descending order
    # You can implement this function either recursively
    # or iteratively


def agnostic_binary_search(arr, target):
    pass
    # Your code here
