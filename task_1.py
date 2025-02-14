def find_min_max(arr_arg):
    """
    Function to find the minimum and maximum values in an array
    using the "divide and conquer" approach.
    """
    # Base case: if only one element, return it as both min and max
    if len(arr_arg) == 1:
        return arr_arg[0], arr_arg[0]

    # Base case: if two elements, return the min and max directly
    if len(arr_arg) == 2:
        return (arr_arg[0], arr_arg[1]) if arr_arg[0] < arr_arg[1] else (arr_arg[1], arr_arg[0])

    # Divide the array into two halves
    mid = len(arr_arg) // 2
    left_min, left_max = find_min_max(arr_arg[:mid])
    right_min, right_max = find_min_max(arr_arg[mid:])

    # Combine results from left and right halves
    overall_min = min(left_min, right_min)
    overall_max = max(left_max, right_max)

    return overall_min, overall_max


if __name__ == "__main__":
    # Test usage
    arr = [3, 1, 7, 5, 9, 2, 8, 4, 6]
    min_val, max_val = find_min_max(arr)
    print(f"Minimum: {min_val}, Maximum: {max_val}")
