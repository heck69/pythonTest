def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
x = int(input("Enter a non-negative integer: "))
result = factorial(x)
print(f"factorial of  {x} is {result}")