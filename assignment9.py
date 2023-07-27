from operations import *

def main():
    # File operations
    file_path = "karan.txt"
    content = "Hello, Karan."
    FileOperations.write_file(file_path, content)
    read_content = FileOperations.read_file(file_path)
    print("Read content:", read_content)

    append_content = " Welcome to python"
    FileOperations.append_file(file_path, append_content)
    read_content = FileOperations.read_file(file_path)
    print("Appended content:", read_content)

    # Mathematical operations
    a = 10
    b = 5
    result_add = MathOperations.add(a, b)
    result_subtract = MathOperations.subtract(a, b)
    result_multiply = MathOperations.multiply(a, b) 
    try:
        result_divide = MathOperations.divide(a, 0)
        print(f"Division result: {result_divide}")
    except ZeroDivisionError as e:
        print("Error:", e)

    # String operations
    input_string = "This is a sample string."
    delimiter = " "
    result_split = StringOperations.split_string(input_string, delimiter)
    print("Split result:", result_split)
    print(f"Addition result: {result_add}")
    print(f"Subtraction result: {result_subtract}")
    print(f"Multiplication result: {result_multiply}")
main()

