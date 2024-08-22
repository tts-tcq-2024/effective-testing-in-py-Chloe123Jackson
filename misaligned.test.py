import unittest
import misaligned
from unittest.mock import patch

class Misaligned_test(unittest.TestCase):
  @patch("misaligned.print_row")
  def fake_print_colour_map(row_number,major,minor,mock_print_row):
    global misaligned.table_mock
    table_mock.append([row_number,major,minor])
    mock_print_row.returnvalue = table_mock
    assert misaligned.create_colour_code_table() == misaligned.print_color_map()
