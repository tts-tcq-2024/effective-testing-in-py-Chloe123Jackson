MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]
table_mock=[]
i=0

from unittest.mock import patch, Mock

def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(MAJOR_COLORS):
        for j, minor in enumerate(MINOR_COLORS):
            print_row(i * 5 + j,major, minor)
    return len(major_colors) * len(minor_colors)

def print_row(row_number,major,minor):
    print(f'{row_number} | {major} | {minor}')
    

@patch("misaligned.print_row")
def fake_print_colour_map(row_number,major,minor,mock_print_row):
    mock_print_row.return_value=table_mock.append([row_number,major,minor])
    return table_mock

def create_colour_code_table():
    row=[]
    table=[]
    pair_number=1
    for major in MAJOR_COLORS:
        for minor in MINOR_COLORS:
            row.append(pair_number)
            row.append(major)
            row.append(minor)
            table.append(row)
            pair_number+=1
            row=[]
    return table

# result = print_color_map()
# assert(result == 25)
ref_table=create_colour_code_table()
# print(ref_table)
result=print_color_map()
# print(result)
# assert table == ref_table
print("All is well (maybe!)\n")
