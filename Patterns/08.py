
# *********
#  *******
#   *****
#    ***
#     *

n = 5

for i in range(n):
    #space
    for j in range(i):
        print(" ", end="")
    #stars
    for j in range(2*(n-i)-1):
        print("*", end="")
    #space
    for j in range(i):#(OPTIONAL LOOP)
        print(" ", end="")
    print()