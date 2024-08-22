MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]
i=0
import unittest
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

class Misaligned_test(unittest.TestCase):
    @patch('misaligned.print_color_map')
    def fake_print_colour_map(self,mock_print_colour_map):
        table_mock=[]
        major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
        minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
        for i, major in enumerate(major_colors):
            for j, minor in enumerate(minor_colors):
                table_mock.append([i * 5 + j,major,minor])
        mock_print_colour_map.return_value=table_mock
        output_table=print_color_map()
        print("Output_table",output_table)
        ref_table=create_colour_code_table()
        print("Ref_table",ref_table)
        self.assertEqual(ref_table,table_mock)
        # assert misaligned.create_colour_code_table() == table_mock

result = print_color_map()
assert(result == 25)

# assert fake_print_colour_map() == True
print("All is well (maybe!)\n")
