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
    ref_table=misaligned.create_colour_code_table()
    self.assertEqual(ref_table,output_table)

if __name__ == '__main__':
  unittest.main()
