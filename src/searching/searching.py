# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # find middle value from list
    # if target > middle value then call function again with new start and end values
    # if target < middle value then call function again with new start and end values
    middle = (start + end) // 2

    if len(arr) == 0:
        return -1

    if target == arr[middle]:
        return middle
    elif target > arr[middle]:
        lowest = middle + 1
        return binary_search(arr, target, lowest, end)
    elif target < arr[middle]:
        highest = middle - 1
        return binary_search(arr, target, start, highest)

    # STRETCH: implement an order-agnostic binary search
    # This version of binary search should correctly find
    # the target regardless of whether the input array is
    # sorted in ascending order or in descending order
    # You can implement this function either recursively
    # or iteratively


def agnostic_binary_search(arr, target):
    pass
    # Your code here
