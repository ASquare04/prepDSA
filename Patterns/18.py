# E
# D E
# C D E
# B C D E
# A B C D E 

n = 5  
for i in range(n):
    for j in range(i, -1, -1):
        print(chr(69 - j), end="")
    print()
