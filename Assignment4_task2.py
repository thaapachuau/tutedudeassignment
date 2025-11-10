def file_operations():
    file_name = "output.txt"

    # 1. Takes user input and writes it to a file named output.txt
    user_initial_input = input("Enter text to write to the file: ")
    with open(file_name, "w") as file:
        file.write(user_initial_input + "\n")
    print(f"Data sucessfully written to '{file_name}'.")

    # 2. Appends additional data to the same file
    additional_data = input("Enter additional text to append: ")
    with open(file_name, "a") as file:
        file.write(additional_data + "\n")
    print(f"Data sucessfully appended")

    # 3. Reads and displays the final content of the file
    print(f"\nFinal content of '{file_name}':")
    with open(file_name, "r") as file:
        final_content = file.read()
        print(final_content)

# Call the function to execute the program
file_operations()