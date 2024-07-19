arr = [1, 2, 3, 4, 5]
n = len(arr)

ascending = True
descending = True

for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        ascending = False
    if arr[i] < arr[i + 1]:
        descending = False

if ascending:
    print("Already Sorted in Ascending Order")
elif descending:
    print("Already Sorted in Descending Order")
else:
    print("Not Sorted")
