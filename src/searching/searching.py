# Runtime complexity: O(n)
def linear_search(arr, target):
    index = 0
    while index < len(arr):
        if arr[index] == target:
            return index
        index += 1

    return -1   # not found


# Runtime complexity: O(log n)
def binary_search(arr, target):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1  # not found
