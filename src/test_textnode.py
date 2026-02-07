import unittest

from textnode import *



class TestTextNode(unittest.TestCase):
    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", node.__repr__()
        )
        
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_ne(self):
        node = TextNode("I'm Paul!", TextType.TEXT)
        node2 = TextNode("I'm Ted!", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_URLisNone(self):
        node = TextNode("boot.dev", TextType.LINK)
        self.assertIsNone(node.url)

    def test_URLisNotNone(self):
        node = TextNode("boot.dev", TextType.LINK, "https://www.boot.dev")
        self.assertIsNotNone(node.url)

    def test_DiffTextType(self):
        node = TextNode("I'm using emphasis!", TextType.ITALIC)
        node2 = TextNode("I'M LOUD!", TextType.BOLD)
        self.assertIsNot(node.text_type, node2.text_type)

    


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

if __name__ == "__main__":
    unittest.main()