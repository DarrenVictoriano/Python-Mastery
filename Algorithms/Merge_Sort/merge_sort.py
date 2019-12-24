"""
Python implementation of Merge Sort algorithmn

Merge two subarrays of arr[]
First subarray is arr[1..m]
Second subarray is [m+1..r]

"""


def merge_sort(arr: list) -> None:
    """
    desc: sort an array in descending order
    parameter: list/array
    return: None - sort the list in memory
    """
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array - floored division
        left_sub = arr[:mid]  # Dividing the array elements
        right_sub = arr[mid:]  # into 2 halves using slice

        merge_sort(left_sub)  # sort the first half
        merge_sort(right_sub)  # sort the second half

        # initialize temp variables to 0 every call
        left_index = 0
        right_index = 0
        arr_index = 0

        # copy data to temp arrays L[] and R[]
        while left_index < len(left_sub) and right_index < len(right_sub):
            if left_sub[left_index] < right_sub[right_index]:
                arr[arr_index] = left_sub[left_index]
                left_index += 1
            else:
                arr[arr_index] = right_sub[right_index]
                right_index += 1
            arr_index += 1

        # Checking if any element was left
        while left_index < len(left_sub):
            arr[arr_index] = left_sub[left_index]
            left_index += 1
            arr_index += 1

        while right_index < len(right_sub):
            arr[arr_index] = right_sub[right_index]
            right_index += 1
            arr_index += 1


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, 3, 5, 2]
merge_sort(alist)
print(alist)
