MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]
table=[]

from unittest.mock import patch

def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)

@patch("builtins.print")
def fake_print_colour_map(mock_print):
    print_colour_map()
    for row in table:
        mock_print.assert_called_with('{:^2} | {:^6} | {:^6} |'.format(*row))
        
    
# def fake_print_colour_map():
#     mock = Mock()
#     for row in table:
#         mock.print_colour_map()
#         mock.print_colour_map.assert_called_with('{:^2} | {:^6} | {:^6} |'.format(*row))

def create_colour_code_table():
    pair_number=1
    row=[]
    for major_colour in MAJOR_COLORS:
        for minor_colour in MINOR_COLORS:
            row.append(pair_number)
            row.append(major_colour)
            row.append(minor_colour)
            table.append(row)
            pair_number+=1
            row=[]

result = print_color_map()
output=fake_print_colour_map()
assert(result == 25)
print("All is well (maybe!)\n")
