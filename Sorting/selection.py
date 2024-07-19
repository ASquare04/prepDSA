# Problem Statement: Given an array of N integers, write a program to implement the Selection sorting algorithm.

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        mini = i
        for j in range(i+1,n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]        
    return arr


num = int(input("Enter the size of the array: "))
arr = [int(input(f"Enter element {i + 1}: ")) for i in range(num)]

print("Array before sorting:", arr)
result = selectionSort(arr)
print("Array after sorting:" , result)
