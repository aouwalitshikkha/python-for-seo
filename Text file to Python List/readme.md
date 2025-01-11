# Text File to Python List

This script reads a text file and converts its contents into a Python list.

## Usage

1. Save the script `text_to_python_list.py` to your local machine.
2. Run the script using Python.
3. When prompted, enter the path to the text file you want to read.

## Example

```python
def text_file_to_list(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    result = text_file_to_list(file_path)
    print(result)
```

## How to Run

1. Open a terminal or command prompt.
2. Navigate to the directory where `text_to_python_list.py` is saved.
3. Run the script using the following command:

```sh
python text_to_python_list.py
```

4. Enter the path to your text file when prompted.

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License.
