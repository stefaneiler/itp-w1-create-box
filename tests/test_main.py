import unittest

from create_box import create_box
from create_box import create_border_box


first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()

fourth_box_expected = """
$$$$$
$   $
$   $
$$$$$
""".lstrip()

fifth_box_expected = """
%%%%%%%%%%
%        %
%        %
%        %
%%%%%%%%%%
""".lstrip()

class TestCreateBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_box(3, 4, '*'), first_box_expected)

    def test_small_box(self):
        self.assertEqual(create_box(1, 1, '@'), second_box_expected)
        
    def test_we_made(self):
        self.assertEqual(create_box(3, 24, 'x'), third_box_expected)


class TestCreateBorderBox(unittest.TestCase):
    def test_border_box(self):
        self.assertEqual(create_border_box(4, 5, '$'), fourth_box_expected)
    
    def test_border_box2(self):
        self.assertEqual(create_border_box(5, 10, '%'), fifth_box_expected)
        
        

        
        