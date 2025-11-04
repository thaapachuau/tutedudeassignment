try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
else:
    # 2. Check whether the number is even or odd using an if-else statement
    if number % 2 == 0:
        # 3. Display the result accordingly
        print(f"{number} is an even number.")
    else:
        # 3. Display the result accordingly
        print(f"{number} is an odd number.")