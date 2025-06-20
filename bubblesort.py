arr = []
n = int(input("number of terms: "))

for i in range(n):
    elements = int(input(f"enter element {i+1}: "))
    arr.append(elements)

print("array: ", arr)

for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            
print("sorted array: ", arr)



    
