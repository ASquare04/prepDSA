
# A  
# B  B
# C  C  C
# D  D  D  D
# E  E  E  E  E

n = 5 
char = 65  
for i in range(n):
    for j in range(i + 1):
        print(chr(char), " ", end="")
    print()
    char = char + 1