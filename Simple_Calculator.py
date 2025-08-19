def calculator():
    import math
    
    print("Advanced Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exponent")

    while True:
        choice = input("Enter choice (1-6): ")
        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print("Result:", num1 + num2)
                elif choice == '2':
                    print("Result:", num1 - num2)
                elif choice == '3':
                    print("Result:", num1 * num2)
                elif choice == '4':
                    if num2 == 0:
                        print("Error! Division by zero.")
                    else:
                        print("Result:", num1 / num2)
                elif choice == '5':
                    print("Result:", num1 % num2)
                elif choice == '6':
                    print("Result:", num1 ** num2)

                again = input("Perform another calculation? (yes/no): ")
                if again.lower() != 'yes':
                    print("Goodbye!")
                    break

            except ValueError:
                print("Please enter valid numbers.")

        else:
            print("Invalid input! Choose from 1 to 6.")
