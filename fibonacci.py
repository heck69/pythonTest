def fibonacci(n):
    if n < 0:
        raise ValueError("should be greater than or equal to 0")
    if n ==0:
        return 0
    elif n ==1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n+2):
            print(a, end=" ")
            a, b = b, a + b
              
    

x = int(input("Enter number of terms: "))
result = fibonacci(x)
