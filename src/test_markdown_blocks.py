import unittest

from markdown_blocks import *

class TestSplitBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_block_to_block_type_Heading(self):
        md = "# This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType("heading")
        )

    def test_block_to_block_type_Heading1(self):
        md = "#### This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType("heading")
        )

    def test_block_to_block_type_InvalidHeading(self):
        md = "############# This is a heading"
        block_type = block_to_block_type(md)
        self.assertNotEqual(
            block_type,
            BlockType("heading")
        )

    def test_block_to_block_type_Code(self):
        md = """
```
function test() {
  console.log("notice the blank line before this function?");
}
```
"""
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType("code")
        )

    def test_block_to_block_type_InvalidCode(self):
        md = """
```
function test() {
  console.log("notice the blank line before this function?");
}
"""
        block_type = block_to_block_type(md)
        self.assertNotEqual(
            block_type,
            BlockType("code")
        )

    def test_block_to_block_type_Quote(self):
        md = "> Quote 1  \n> Quote 2  \n> Quote 3  "
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType("quote")
        )

    def test_block_to_block_type_InvalidQuote(self):
        md = "> Quote 1  \nQuote 2  \nQuote 3  "
        block_type = block_to_block_type(md)
        self.assertNotEqual(
            block_type,
            BlockType("quote")
        )

    def test_block_to_block_type_UnorderedList(self):
        md = "- pine  \n- apple  \n- pineapple  "
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType("unordered")
        )


    def test_block_to_block_type_InvalidUnorderedList(self):
        md = "pine  \napple  \n- pineapple  "
        block_type = block_to_block_type(md)
        self.assertNotEqual(
            block_type,
            BlockType("unordered")
        )

    def test_block_to_block_type_OrderedList(self):
        md = "1. pine \n2. apple \n3. pineapple "
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType("ordered")
        )


    def test_block_to_block_type_OrderedList(self):
        md = "1. pine \n1. apple \n1. pineapple "
        block_type = block_to_block_type(md)
        self.assertNotEqual(
            block_type,
            BlockType("ordered")
        )

    def test_block_to_block_type_Paragraph(self):
        md = "Apple bottom jeans, boots with the fur"
        block_type = block_to_block_type(md)
        self.assertEqual(
            block_type,
            BlockType("paragraph")
        )
