#Problem Statement: Given an array, we have to find the largest element in the array.


#1
num = [12, 6, 8, 23, 18]
maxi = float('-inf')

for i in num:
    if i > maxi:
        maxi = i

print(maxi)

#2
from typing import List
def sortArr(arr: List[int]) -> int:
    arr.sort()
    return arr[-1]
if __name__ == "__main__":
    arr1 = [2, 5, 1, 3, 0]
    arr2 = [8, 10, 5, 7, 9]
    print("The Largest element in the array is:", sortArr(arr1))
    print("The Largest element in the array is:", sortArr(arr2))


#3
def findLargestElement(arr, n):
    max = arr[0]
    for i in range(0, n):
        if (max < arr[i]):
            max = arr[i]
    return max


if __name__ == "__main__":
    arr1 = [2, 5, 1, 3, 0]
    n = 5
    max = findLargestElement(arr1, n)
    print("The largest element in the array is:", max)