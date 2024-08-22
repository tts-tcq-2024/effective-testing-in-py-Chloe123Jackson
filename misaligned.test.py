import unittest
import misaligned
from unittest.mock import patch

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
    output_table=misaligned.print_color_map()
    print("Output_table",output_table)
    ref_table=misaligned.create_colour_code_table()
    print("Ref_table",ref_table)
    self.assertEqual(ref_table,table_mock)
  # assert misaligned.create_colour_code_table() == table_mock

# class Misaligned_test(unittest.TestCase):
#   @patch("builtins.print")
#   def fake_print_colour_map(self,mock_print_colour_map):
#     misaligned.print_color_map()
#     mock_print_colour_map.assert_called_with("")
#     table_mock=[]
#     major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
#     minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
#     for i, major in enumerate(major_colors):
#         for j, minor in enumerate(minor_colors):
#             table_mock.append([i * 5 + j,major,minor])
#     mock_print_colour_map.return_value=table_mock
#     output_table=misaligned.print_color_map()
#     print("Output_table",output_table)
#     ref_table=create_colour_code_table()
#     print("Ref_table",ref_table)
#     self.assertEqual(ref_table,table_mock)
  # assert misaligned.create_colour_code_table() == table_mock

if __name__ == '__main__':
  unittest.main()
  print("Hello")
