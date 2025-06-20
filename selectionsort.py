n = int(input("Enter number of terms: "))
arr = []

for i in range(n):
    e = int(input(f"Enter element {i+1}: "))
    arr.append(e)
    
print("array: ", arr)

for i in range(n):
    min_index = i
    for j in range (i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
    
print("sorted array: ", arr)
    
         