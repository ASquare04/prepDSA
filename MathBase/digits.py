#Problem Statement: Given an integer N, return the number of digits in N.

num = int(input("Enter any number: "))
if num == 0:
    print(1)
else:
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    print(count)
