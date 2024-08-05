import unittest.mock
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
            break
        break
    return len(major_colors) * len(minor_colors)
    


def fake_print_colour_map():
    mock = Mock()
    mock.print_colour_map()
    mock.method.assert_called_with('0 | White | Blue')

result = print_color_map()
output=fake_print_colour_map()
assert(result == 25)
print("All is well (maybe!)\n")
