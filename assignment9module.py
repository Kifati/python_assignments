import math

class FileOperations: 
    def read_file(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    def write_file(file_path, content):
        with open(file_path, 'w') as file:
            file.write(content) 
    def append_file(file_path, content):
        with open(file_path, 'a') as file:
            file.write(content)

class MathOperations: 
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    def multiply(a, b):
        return a * b
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

class StringOperations:
    def split_string(input_string, delimiter):
        return input_string.split(delimiter)

