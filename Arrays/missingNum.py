# Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find the number(between 1 to N), that is not present in the given array.

def find_missing_number(arr):
    n = len(arr) + 1
    
    expected_sum = n * (n + 1) // 2
    
    actual_sum = sum(arr)
    
    missing_number = expected_sum - actual_sum
    
    return missing_number

# Example usage
arr = [9, 6, 4, 2, 3, 5, 7, 0, 1]

missing_number = find_missing_number(arr)

print(f"The missing number is: {missing_number}")
