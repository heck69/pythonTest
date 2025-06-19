 


while True:
    a = int(input("Enter First Number:"))
    b = int(input("Enter Second Number:")) 
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter choice (1/2/3/4): ")
    if choice == '1':
        print(f"{a} + {b} = {a + b}")
    elif choice == '2':
        print(f"{a} - {b} = {a - b}")           
    elif choice == '3':
        print(f"{a} * {b} = {a * b}")
    elif choice == '4':
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input. Please enter a valid choice (1/2/3/4).")
        continue
    
    intention = int(input("Press 1 to continue or 0 to exit: "))
    if intention == 0:
        print("Exiting the calculator. Goodbye!")
        break
    else:
        continue
    break