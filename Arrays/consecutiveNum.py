# Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

price = [1, 1, 0, 1, 1, 1]

current_count = 0
max_count = 0

for i in price:
    if i == 1:
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0

print(max_count)
