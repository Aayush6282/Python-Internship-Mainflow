# Calculator Program
# Step 1: Designing the User Interface
def main():
    print("Welcome to the Simple Calculator!")

    while True:
        try:
            # User input numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # User input the operation
            print("Select operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            operation = input("Enter your choice (1/2/3/4): ")

            # Step 2: Perform the chosen operation using if-elif
            if operation == '1':
                result = add(num1, num2)
                print(f"The result of addition is: {result}")
            elif operation == '2':
                result = subtract(num1, num2)
                print(f"The result of subtraction is: {result}")
            elif operation == '3':
                result = multiply(num1, num2)
                print(f"The result of multiplication is: {result}")
            elif operation == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = divide(num1, num2)
                    print(f"The result of division is: {result}")
            else:
                print("Invalid operation choice. Please choose 1, 2, 3, or 4.")
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        # Asking user if they want to perform another calculation or want to quit
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

# Step 3: Implement Arithmetic Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Run the calculator
if __name__ == "__main__":
    main()
