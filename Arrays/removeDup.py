# Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

def remove_duplicates(arr):
    seen = set()
    result = []
    
    for i in arr:
        if i not in seen:
            seen.add(i)
            result.append(i)
    
    return result

arr = [1, 3, 1, 2, 4, 5, 2, 6, 4, 7]
print(remove_duplicates(arr))
        
        
        
from typing import List

def removeDuplicates(arr: List[int]) -> int:
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 3]
    k = removeDuplicates(arr)
    print("The array after removing duplicate elements is ")
    for i in range(k):
        print(arr[i], end=" ")
        
