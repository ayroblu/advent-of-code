import os


def read_input(current_file_path: str) -> str:
    return read_file(current_file_path, "input")


def read_file(current_file_path: str, relative_file_name: str) -> str:
    """current_file_path should be __file__"""

    current_file_path = os.path.abspath(current_file_path)

    file_to_read = os.path.join(os.path.dirname(current_file_path), relative_file_name)

    with open(file_to_read) as f:
        file_contents = f.read()

    return file_contents
