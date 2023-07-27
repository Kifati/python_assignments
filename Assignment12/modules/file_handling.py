def read_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ""

def write_data(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)

def append_data(file_path, data):
    with open(file_path, 'a') as file:
        file.write(data + "\n")
