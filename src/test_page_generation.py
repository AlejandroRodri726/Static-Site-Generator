import unittest
from page_generation import *

class TestTextNode(unittest.TestCase):
    def test_extract_title(self):
        title = extract_title("# Hello    \n")
        self.assertEqual(
            title,
            "Hello"
        )

    #def test_extract_title_Invalid(self):
        #title = extract_title("### Hello    \n")
        