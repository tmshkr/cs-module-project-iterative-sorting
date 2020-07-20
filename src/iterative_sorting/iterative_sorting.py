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
            # as long as it is smaller than the current smallest
            if arr[j] < arr[min_index]:
                min_index = j
        # swap the element at i with the element at min_index
        arr[i], arr[min_index] = arr[min_index], arr[i]
    # return the sorted array
    return arr


# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # Your code here
    pass


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


def counting_sort(arr, maximum=None):
    # Your code here
    pass
