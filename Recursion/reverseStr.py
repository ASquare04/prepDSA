# def reverse(s):
# 	str = ""
# 	for i in s:
# 		str = i + str
# 	return str

# s = "ASPHALT"

# print("The original : ", end="")
# print(s)

# print("The reversed is : ", end="")
# print(reverse(s))


def isPalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

s = "ARORA"
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")
