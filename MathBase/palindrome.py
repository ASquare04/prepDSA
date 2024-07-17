#Problem Statement: Given an integer N, return true if it is a palindrome else return false.

num = int(input("Enter any number"))

orgNum = num

reverse=0
while num>0:
    digit = num % 10
    reverse = reverse * 10 + digit 
    num = num//10
    
if orgNum == reverse:
    print("A PALINDROME")
else:
    print("NOT A PALINDROME")