# Problem Statement: Given an integer N, return true it is an Armstrong number otherwise return false.
# An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

num = int(input("Enter any number"))
orgNum = num

p = len(str(num))
n=0

while num>0:
    digit = num%10
    n = n + pow(digit, p)
    num =  num//10
    
if n == orgNum:
    print("ARMSTRONG NUMBER",n)
else:
    print("NOT ARMSTRONG")    