"""
Python implementation of  Quicksort algorithmn

1. Pick a Pivot
2. Partition the array into two subarrays:
    elements less than the pivot and elements greater than the pivot
3. Call Quicksort recursively on the two sub-array
"""


def quicksort(arr: list) -> list:
    """ takes unsorted list and return a sorted list"""
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # set pivot as the middle of the array
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([3, 1, 2, 8, 3, 6]))
