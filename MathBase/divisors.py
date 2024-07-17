# Problem Statement: Given an integer N, return all divisors of N.

num = int(input("Enter the number"))
arr = []
for i in range(1,num+1):
    if num%i==0:
        arr.append(i)

print(arr)