# Problem Statement: Given an array of N integers, write a program to implement the Bubble Sorting algorithm.

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False  # Initialize swapped as False at the beginning of each pass
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True  # Set swapped to True if a swap occurs
        if not swapped:
            break  # If no swaps occurred in the inner loop, the array is already sorted
    return arr

num = int(input("Enter the size of the array: "))
arr = [int(input(f"Enter element {i + 1}: ")) for i in range(num)]

print("Array before sorting:", arr)
result = bubbleSort(arr)
print("Array after sorting:" , result)

#Time Complexity 

# (Without Use of Flag)
# Because a bubble sort relies on two nested loops, its time complexity is O(n^2), which means while it can be acceptable for small sets of data    

# (With Use of Flag)
# In the best-case scenario (already sorted array), the algorithm will terminate after making a single pass through the array, resulting in 𝑂(𝑛) time complexity.

# Space Complexity: O(1)