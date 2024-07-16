n = 5
char = 65
for i in range(n):
    #space
    for j in range(n-i-1):
        print(" ", end="")
    #stars
    for j in range(2*i+1):
        print(chr(char), end="")
    #space
    for j in range(n-i-1):#(OPTIONAL LOOP)
        print(" ", end="")
    print()