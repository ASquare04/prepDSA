
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

n = 5

# for i in range(n):
#     for j in range(i + 1):
#         print("*", end="")
#     print()


# for i in range(n - 1):
#     for j in range(n - i - 1):
#         print("*", end="")
#     print()

for i in range(2*n-1):
    stars = i
    if(i>n):
        stars = 2*n-i
    for j in range(stars):
        print("*", end="")
    print()


