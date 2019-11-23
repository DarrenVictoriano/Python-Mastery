"""
Python implementation of Merge Sort algorithmn

Merge two subarrays of arr[]
First subarray is arr[1..m]
Second subarray is [m+1..r]

"""


def merge_sort(arr: list) -> list:
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves using slice

        merge_sort(L)  # sort the first half
        merge_sort(R)  # sort the second half

        # initialize temp variables to 0 every call
        i = j = k = 0

        # copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
