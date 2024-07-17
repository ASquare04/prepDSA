# Problem Statement: Given a number X,  print its factorial.

# num = int(input("Enter the range"))
# fact = 1
# for i in range(1,num+1):
#     fact = fact * i
# print(fact)

def calcFactorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num * calcFactorial(num - 1)
    

num = int(input("Enter the range"))
result = calcFactorial(num)
print(result)