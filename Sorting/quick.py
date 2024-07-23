def quick_sort(arr):
    # Base case: an array of zero or one element is already sorted
    if len(arr) <= 1:
        return arr

    # Choose the pivot element. Here we choose the last element as pivot
    pivot = arr[len(arr) // 2]

    # Partition the array into three parts:
    # 1. Elements less than the pivot
    # 2. Elements equal to the pivot
    # 3. Elements greater than the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively apply the quick_sort to the left and right parts
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    sorted_arr = quick_sort(arr)
    print("Sorted array:", sorted_arr)
