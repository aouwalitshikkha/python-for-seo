def text_file_to_list(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    result = text_file_to_list(file_path)
    print(result)