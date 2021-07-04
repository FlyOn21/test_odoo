from typing import NoReturn


def characters_pyramid(pyramid_params: str) -> NoReturn:
    """Function implements counting printable characters
     and drawing a pyramid from these characters.
     The function accepts a string as input,
     which consists of the desired character and the
     height of the pyramid separated by a space.
     Example: "@ 9" """
    char_param, height_param = pyramid_params.split(" ")
    height = int(height_param)
    if check_height_param(height):
        pyramid_level_list = []
        counter = 0
        n = 0
        for step in range(1, height + 1):
            char_in_pyramid_level = n * 2 + 1
            number_of_spaces = height - (n + 1)
            pyramid_level = (number_of_spaces * " ") + (char_param * char_in_pyramid_level)
            counter += len(pyramid_level)
            pyramid_level_list.append(pyramid_level)
            n += 1
        print(counter)
        for pyramid_level in pyramid_level_list:
            print(pyramid_level)
    else:
        print("The height parameter does not meet the condition")


def check_height_param(height: int) -> bool:
    """Checks if the given height of the pyramid
    satisfies the constraints specified in the condition"""
    if height > 50:
        return False
    return True


if __name__ == "__main__":
    characters_pyramid("@ 9")
