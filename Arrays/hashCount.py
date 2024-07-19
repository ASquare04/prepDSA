# Problem statement: Given an array, we have found the number of occurrences of each element in the array.

# def countFreq(arr, n):
#     visited = [False] * n
#     for i in range(n):
#         if (visited[i] == True):
#             continue
#         count = 1
#         for j in range(i + 1, n):
#             if (arr[i] == arr[j]):
#                 visited[j] = True
#                 count += 1
#         print(arr[i], count)


# if __name__ == "__main__":
#     arr = [10,5,10,15,10,5]
#     n = len(arr)
#     countFreq(arr, n)    


arr = [10, 15, 10, 10, 15, 30]
record = {}


for i in arr:
    if i in record:
        record[i] += 1
    else:
        record[i] = 1

print("Frequencies:", record)


highest_freq = None

lowest_freq = None


for value in record.values():
    if highest_freq is None or value > highest_freq:
        highest_freq = value
    if lowest_freq is None or value < lowest_freq:
        lowest_freq = value

highest_freq_elements = []
lowest_freq_elements = []

for key, value in record.items():
    if value == highest_freq:
        highest_freq_elements.append(key)
    if value == lowest_freq:
        lowest_freq_elements.append(key)

print("Highest frequency elements:", highest_freq_elements)
print("Lowest frequency elements:", lowest_freq_elements)



    # max_freq = 0
    # min_freq = len(arr)
    # max_ele = None
    # min_ele = None


    # for element, count in record.items():
    #     if count > max_freq:
    #         max_ele = element
    #         max_freq = count
    #     if count < min_freq:
    #         min_ele = element
    #         min_freq = count

    
