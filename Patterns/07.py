
#     *
#    ***
#   *****
#  *******
# *********

# [4,1,4]
# [3,3,3]
# [2,5,2]
# [1,7,1]
# [0,9,0]
#[n-i-1] , [2*i+1] , [n-i-1]

n = 5

for i in range(n):
    #space
    for j in range(n-i-1):
        print(" ", end="")
    #stars
    for j in range(2*i+1):
        print("*", end="")
    #space
    for j in range(n-i-1):#(OPTIONAL LOOP)
        print(" ", end="")
    print()