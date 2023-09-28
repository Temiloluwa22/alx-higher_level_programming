#!/usr/bin/python3
# a function that finds a peak in the list of integers


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers using a binary search-like approach.
    
    Args:
    list_of_integers (list): List of unsorted integers.

    Returns:
    int: The peak element found in the list.
    """
    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        # Compare the middle element with its neighbors
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    # At the end of the loop, 'left' points to a peak element
    return list_of_integers[left]
