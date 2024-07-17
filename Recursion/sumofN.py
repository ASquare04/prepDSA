# Problem statement: Given a number ‘N’, find out the sum of the first N natural numbers.

# n = int(input("Enter the range"))

# summ1 = n * (n+1) // 2
# print(summ1)

# summ2 = 0

# for i in range(1,n+1):
#     summ2 = summ2+i
# print(summ2)


def summ(n):
    if n == 0:
        return 0
    else:
        return n + summ(n - 1)

# Example usage:
n = int(input("Enter the range: "))
result = summ(n)
print(f"The sum of the first {n} natural numbers is: {result}")
