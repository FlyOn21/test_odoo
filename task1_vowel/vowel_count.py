import os


def open_file(filename: str) -> str:
    """Implemented open source file"""
    with open(os.path.abspath(filename), mode="r", encoding="UTF8") as file:
        data = file.read()
        return data


def check_line_length(text_data: str) -> bool:
    """Checking the length of the input string"""
    if len(text_data) > 100:
        return False
    return True


def main(filename: str) -> int:
    """Main function. Start process counting
    vowel character in source file.
    Accepts source file name"""
    counter = 0
    vowel_char = ("A", "E", "I", "O", "U", "Y")
    text_data = open_file(filename)
    if not check_line_length(text_data):
        return "The length of the line does not meet the requirements"
    for char in text_data.upper():
        if char in vowel_char:
            counter += 1
    return counter


if __name__ == "__main__":
    result = main("text.txt")
    print(result)
