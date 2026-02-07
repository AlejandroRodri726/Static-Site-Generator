import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"}
        )
        self.assertEqual(
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})", 
            node.__repr__()
        )


    def test_values(self):
        node = HTMLNode(
            "div", 
            "I wish I could read",
            None,
            None
        )
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I wish I could read")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)


    def test_props_to_html(self):
        node = HTMLNode(
            "p", 
            "value",
            None,
            {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            " href=\"https://www.google.com\" target=\"_blank\"", 
            node.props_to_html()
        )


    def test_leaf_to_html_p(self):
        node = LeafNode(
            "p", 
            "Hello, world!",
            None
        )
        self.assertEqual("<p>Hello, world!</p>", node.to_html(), )


    def test_leaf_to_html_a(self):
        node = LeafNode(
            "a", 
            "Click me!", 
            {"href": "https://www.google.com"}
        )
        self.assertEqual(
            "<a href=\"https://www.google.com\">Click me!</a>",
            node.to_html()
        )


    def test_leaf_to_html_no_tag(self):
        node = LeafNode(
            None, 
            "Hello, world!",
            None)
        self.assertEqual("Hello, world!", node.to_html(), )


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child", None)
        parent_node = ParentNode("div", [child_node], None)
        self.assertEqual(
            "<div><span>child</span></div>",
            parent_node.to_html()
        )


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            "<div><span><b>grandchild</b></span></div>",
            parent_node.to_html()
        )


    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
            node.to_html()
        )


    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
            node.to_html()
        )



if __name__ == "__main__":
    unittest.main()