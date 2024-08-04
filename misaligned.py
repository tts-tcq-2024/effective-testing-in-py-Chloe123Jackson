from unittest.mock import patch
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)

@patch('builtins.print')
def fake_print_colour_map():
    print_color_map()
    fake_print_colour_map.assert_called_with('2')


result = print_color_map()
assert(result == 25)
print("All is well (maybe!)\n")
