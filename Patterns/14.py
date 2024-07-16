# A
# A B
# A B C
# A B C D
# A B C D E

n = 5  
for i in range(n):
    char = 65 
    for j in range(i + 1):
        print(chr(char), " ", end="")
        char += 1
    print()
