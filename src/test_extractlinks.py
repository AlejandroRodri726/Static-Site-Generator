import unittest

from node_functions import *

class TestExtractLinks(unittest.TestCase):
    def test_ExtractMDImage_(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            matches,
            [
                ("image", "https://i.imgur.com/zjjcJKZ.png"),
            ]
        )
        
    def test_ExtractMDImage_Multi(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) " \
        "and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            matches,
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"), 
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ]
        )


    def test_ExtractMDLink(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and " \
        "[to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            matches,
            [
                ("to boot dev", "https://www.boot.dev"), 
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ]
        )
