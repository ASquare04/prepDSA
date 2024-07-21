# Problem Statement: Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.

def linearSearch(arr,num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    
arr = [12,42,21,54,35]
num = 54

result = linearSearch(arr,num)
print("Element present at Index",result)
g