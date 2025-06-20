arr = []
n = int(input("Enter no.of digits: "))

for i in range(n):
    e = int(input(f"Enter element {i+1}: "))
    arr.append(e)
print("array: ", arr)

for i in range (1, n):
    key = arr[i]
    j = i-1
    while j>=0 and key<arr[j]:
        arr[j+1] = arr[j]
        j -=1
    arr[j+1] = key
    
print("sorted array: ", arr )