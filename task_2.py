import random


def quick_select(arr, k):
    """
    Finds the k-th smallest element in an unsorted array using Quick Select.

    :param arr: List of numbers
    :param k: The index (1-based) of the smallest element to find
    :return: The k-th smallest element
    """
    if len(arr) == 1:
        return arr[0]

    # Select a random pivot element
    pivot = random.choice(arr)

    # Partition the array into three parts
    left = [x for x in arr if x < pivot]  # Elements smaller than pivot
    equal = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    # Determine where the k-th smallest element is
    if k <= len(left):  # It's in the left partition
        return quick_select(left, k)
    elif k <= len(left) + len(equal):  # It's the pivot itself
        return pivot
    else:  # It's in the right partition
        return quick_select(right, k - len(left) - len(equal))


if __name__ == "__main__":
    # Test usage
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    print(f"The {k}-th smallest element is: {quick_select(arr, k)}")
