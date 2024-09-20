# file_handling_assignment.py

# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("Line 1: Hello, World!\n")
        file.write("Line 2: The number is 42\n")
        file.write("Line 3: Python is fun!\n")
    print("File created and initial lines written successfully.")
except Exception as e:
    print(f"An error occurred during file creation: {e}")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
    print("File content after initial write:")
    print(content)
except FileNotFoundError:
    print("File not found. Please ensure the file exists.")
except PermissionError:
    print("Permission denied. Please check your file permissions.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Line 4: Appending new line 1\n")
        file.write("Line 5: Appending new line 2\n")
        file.write("Line 6: Appending new line 3\n")
    print("Additional lines appended successfully.")
except Exception as e:
    print(f"An error occurred during file appending: {e}")

# Reading and Displaying the updated content
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
    print("File content after appending:")
    print(content)
except FileNotFoundError:
    print("File not found. Please ensure the file exists.")
except PermissionError:
    print("Permission denied. Please check your file permissions.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
finally:
    print("File operations completed.")
