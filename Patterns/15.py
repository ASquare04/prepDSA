# A B C D E
# A B C D
# A B C
# A B
# A

n = 5  
for i in range(n,0,-1):
    char = 65
    for j in range(i):
        print(chr(char), " ", end="")
        char += 1
    print()
