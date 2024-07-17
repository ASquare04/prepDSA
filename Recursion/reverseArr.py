# Problem Statement: You are given an array. The task is to reverse the array and print it. 

# arr1 = [12, 24, 36, 48, 60]
# arr2 = []

# for i in range(len(arr1)-1, -1, -1):
#     arr2.append(arr1[i])

# print("Original array:", arr1)
# print("Reversed array:", arr2)


def reverse_array(arr, start, end):
    if start >= end:
        return
    
    arr[start], arr[end] = arr[end], arr[start]

    reverse_array(arr, start + 1, end - 1)

arr1 = [12, 24, 36, 48, 60]
print("Original array:", arr1)
reverse_array(arr1, 0, len(arr1) - 1)
print("Reversed array:", arr1)
