import unittest
import misaligned
from unittest.mock import patch

class Misaligned_test(unittest.TestCase):
  @patch("misaligned.print_color_map")
  def fake_print_colour_map(self,mock_print_colour_map):
    global table_mock
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(MAJOR_COLORS):
        for j, minor in enumerate(MINOR_COLORS):
            table_mock.append([i * 5 + j,major,minor])
    mock_print_colour_map.returnvalue=table_mock
  assert misaligned.create_colour_code_table() == table_mock
