MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]
table=[]
table_mock=[]
i=0

from unittest.mock import patch, Mock

def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print_row(i * 5 + j,major, minor)
    return len(major_colors) * len(minor_colors)

def print_row(row_number,major,minor):
    
    print(f'{row_number} | {major} | {minor}')
    

@patch("print_row")
def fake_print_colour_map(mock_print_row):
    for i, major in enumerate(MAJOR_COLORS):
        for j, minor in enumerate(MINOR_COLORS):
            mock_print_row.return_value=table_mock.append([i*5+j,major,minor])
            
        
    
# def fake_print_colour_map():
#     mock = Mock()
#     for i, major in enumerate(major_colors):
#         for j, minor in enumerate(minor_colors):
#             print(f'{i * 5 + j} | {major} | {minor}')

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
# fake_print_colour_map()
assert(result == 24)
assert(table== print_colour_map)
print("All is well (maybe!)\n")
