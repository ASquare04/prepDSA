#Problem Statement: Given an integer N return the reverse of the given number.

num = int(input("Enter any number"))

reverse=0
while num>0:
    digit = num % 10
    reverse = reverse * 10 + digit 
    num = num//10
    
print(reverse)