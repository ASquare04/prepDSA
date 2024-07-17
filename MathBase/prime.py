# Problem Statement: Given an integer N, check whether it is prime or not. A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2.

num = int(input("Enter any number"))
k=0

for i in range(1,num+1):
    if num % i == 0:
        k = k+1

if k==2:
    print("PRIME")
else:
    print("COMPOSITE")