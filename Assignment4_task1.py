ef read_and_print_file(filename):
    """
    Opens and reads a text file, printing its content line by line.
    Handles FileNotFoundError if the file does not exist.
    """
    try:
        with open(filename, 'r') as file:
            print(f"Content of '{filename}':")
            for line in file:
                print(line.strip())  # .strip() removes leading/trailing whitespace, including newline characters
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function with the desired filename
read_and_print_file("sample.txt")