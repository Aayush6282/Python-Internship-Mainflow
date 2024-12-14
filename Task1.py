Arithmetic Operations

1. Addition:
  a = int(input ("Enter first number:"))
  b = int(input ("Enter second numbdr:"))
  c = a + b
  print("The sum is:",c)

2. Subtraction:
  a = int(input ("Enter first number:"))
  b = int(input ("Enter second numbdr:"))
  c = a - b
  print("The difference is:",c)

3. Multiplication:
  a = float(input ("Enter first number:"))
  b = float(input ("Enter second numbdr:"))
  c = a * b
  print("The product is:",c)

4. Division and Modulus:
  a = float(input ("Enter first number:"))
  b = float(input ("Enter second numbdr:"))
  c = a / b
  d = a % b
  print("The quotient is: ",c)
  print("The remainder is: ",d)

List:
        # Create an empty list
        my_list = []
        
        # Append elements to the list
        my_list.append("Hello")
        my_list.append("hi")
        my_list.append("hey")
        
        print("List : ",my_list)

Tuple:
        # Define a tuple with the specified values
        my_tuple = (5, 4, 4)
        
        # Print the tuple
        print("Tuple : ",my_tuple)
        
Dictionary:
        # Define an empty dictionary
        my_dict = {}
        
        # Take user input for key-value pairs
        num_pairs = int(input("Enter the number of key-value pairs: "))
        for i in range(num_pairs):
            key = i+1 #  = input(f"Enter key {i + 1}: ")
            value = input(f"Enter value for {key}: ")
            my_dict[key] = value
        
        # Print the dictionary
        print("Dictionary:", my_dict)

String Operations:

        # Reverse string
        s = input("Enter the String :")
        print(s[::-1])

        # String Slicing
        s = input("Enter the String :") 
        start = int(input("Starting Index :")) 
        end = int(input("Ending Index :"))
        print(s[start:end])

        # String Concatenation
        s = input("Enter the String :")
        s1 = input("Enter a String :")
        s2 = input("[Optional]Enter a String :") 
        print(s + s1)
        print(s +s1 +s2)

        # String Repitition
        s = input("Enter the String :")
        n = int(input("Enter the Integer :"))
        print((s + "\t")*n)

    Conditional Statements:

    Question - Write a python program that reads in two integers and determines and prints if the first is a multiple of the second
        # Read two integers from the user
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))
        
        # Check if the first number is a multiple of the second number
        if num1 % num2 == 0:
            print(f"{num1} is a multiple of {num2}")
        else:
            print(f"{num1} is not a multiple of {num2}")

    For Loop:
        fruits = ["apple", "banana", "orange", "grape", "kiwi"]
        for fruit in fruits:
            print(fruit)

    While Loop:
        fruits = ["apple", "banana", "orange", "grape", "kiwi"]
        index = 0
        while index < len(fruits):
            # Print the current fruit
            print(fruits[index])
            # Increment the index to move to the next fruit
            index += 1










