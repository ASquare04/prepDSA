# Problem Statement: Given two integers N1 and N2, find their greatest common divisor.

# num1 = int(input("Enter the number 1 :"))
# num2 = int(input("Enter the number 2 :"))

# gcd = 0
# if num1>num2:
#     maxRange = num2
# else:
#     maxRange = num1

# for i in range(1,maxRange+1):
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i

# print("GCD : ", gcd)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))

result = gcd(num1, num2)
print("GCD:", result)

#Euclidean algorithm, which is much faster for finding the GCD:
