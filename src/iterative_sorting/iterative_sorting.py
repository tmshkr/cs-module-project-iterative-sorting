# Selection Sort time complexity: O(n^2)
def selection_sort(arr):
    # go through each item in the array: O(n)
    for i in range(len(arr)):
        # set current min to i
        min_index = i
        # starting at the next element
        for j in range(i+1, len(arr)):
            # go through the array again: O(n)
            # set the smallest item's index to min_index
            if arr[j] < arr[min_index]:
                min_index = j
        # swap the element at i with the element at min_index
        arr[i], arr[min_index] = arr[min_index], arr[i]
    # return the sorted array
    return arr


# Bubble Sort time complexity: O(n^2) (average/worst)
def bubble_sort(arr):
    # go through each item in the array (except the last item)
    for i in range(len(arr)-1):
        # go through the items up to the last i+1 items
        # that will already be sorted
        for j in range(len(arr)-i-1):
            # if the item at j is greater than
            # the item at the next index
            # swap them so that the greatest values
            # bubble up to the end of the array
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # return the sorted array
    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the
buckets.

What is the time and space complexity of the counting sort algorithm?
'''


# Counting Sort time complexity: O(n + k) where k is the range
def counting_sort(arr):
    # if the input array is empty
    # return the empty array
    if len(arr) == 0:
        return arr

    # create a counter array to count the occurrences
    # of each number in the input array
    counter = [0] * (max(arr) + 1)
    for item in arr:
        if item < 0:
            return "Error, negative numbers not allowed in Count Sort"
        counter[item] += 1

    # we'll keep track of the total
    # so that we know how many numbers will come before
    # the number represented by that index
    total = 0
    for i, count in enumerate(counter):
        counter[i] = total
        total += count

    output = [None] * len(arr)

    # now go through each item in the input array
    for num in arr:
        # counter[num] will hold the number of items
        # that come before num, so that it is also
        # the index we should insert num at in the
        # output array
        output[counter[num]] = num

        # so long as we increment the value at counter[num]
        # to the next index to insert at in the output array
        counter[num] += 1

    return output


arr = [8, 7, 1, 2, 2, 2, 7, 3, 9, 8, 2, 1, 4, 2, 4, 6, 9, 2]
