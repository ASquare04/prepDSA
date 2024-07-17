# num = int(input("Enter the range of Series"))

# n1,n2 = 0,1
# print("Fibo Seires",n1,n2,end=" ")
# for i in range(2, num):
#     n3 = n1+n2
#     n1 = n2
#     n2 = n3
#     print(n3 , end = " ")

# print()

def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))  

nterms = int(input("How many terms? "))   
if nterms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(recur_fibo(i))  