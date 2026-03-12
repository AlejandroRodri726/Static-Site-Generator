from enum import Enum
import re
from htmlnode import *
from inline_markdown import *
from textnode import *

class BlockType(Enum):
	PARAGRAPH="paragraph"
	HEADING="heading"
	CODE="code"
	QUOTE="quote"
	ORDERED="ordered"
	UNORDERED="unordered"


def block_to_block_type(markdown):
	if re.search(r"^#{1,6} ", markdown):
		return BlockType("heading")
	elif re.search(r"`{3}\n[\s\S]*`{3}", markdown):
		return BlockType("code")
	elif re.fullmatch(r"(> ?.*\n?)+", markdown):
		return BlockType("quote")
	elif re.fullmatch(r"(- .*\n?)+", markdown):
		return BlockType("unordered")
	
	lines = markdown.split("\n")
	inc = 1
	for line in lines:
		if not line.startswith(f"{inc}. "):
			return BlockType("paragraph")
		inc += 1
		
	return BlockType("ordered")

    
def markdown_to_blocks(markdown):
	block_list = markdown.split("\n\n")
	filtered_blocks = []
	for block in block_list:
		if block == "":
			continue
		filtered_blocks.append(block.strip())
	return filtered_blocks


def block_to_html_node(block):
	block_type = block_to_block_type(block)
	if block_type is BlockType.PARAGRAPH:
		lines = block.split("\n")
		paragraph = " ".join(lines)
		children = text_to_children(paragraph)
		return ParentNode("p", children)

	if block_type is BlockType.HEADING:
		numH = block.count('#')
		if numH > 6:
			raise ValueError(f"invalid heading level: {numH}") 
		text = block[numH + 1:]
		children = text_to_children(text)
		return ParentNode(f"h{numH}", children)

	if block_type is BlockType.CODE:
		if not block.startswith("```") or not block.endswith("```"):
			raise ValueError("invalid code block")
		text_node = TextNode(block[4:-3], TextType.TEXT)
		child = text_node_to_html_node(text_node)
		code = ParentNode("code", [child])
		return ParentNode("pre", [code])

	if block_type is BlockType.QUOTE:
		lines = block.split("\n")
		new_lines = []
		for line in lines:
			if not line.startswith(">"):
				raise ValueError("invalid quote block")
			new_lines.append(line.lstrip(">").strip())
		quote = " ".join(new_lines)
		children = text_to_children(quote)
		return ParentNode("blockquote", children)

	if block_type is BlockType.ORDERED:
		items = block.split("\n")
		html_items = []
		for item in items:
			parts = item.split(". ", 1)
			text = parts[1]
			children = text_to_children(text)
			html_items.append(ParentNode("li", children))
		return ParentNode("ol", html_items)
	
	if block_type is BlockType.UNORDERED:
		items = block.split("\n")
		html_items = []
		for item in items:
			text = item[2:]
			children = text_to_children(text)
			html_items.append(ParentNode("li", children))
		return ParentNode("ul", html_items)
	raise ValueError(f"Invalid text type: {block_type}")

def text_to_children(text):
	html_nodes = []
	text_nodes = text_to_textnodes(text)
	for text_node in text_nodes:
		html_nodes.append(text_node_to_html_node(text_node))
	return html_nodes

def markdown_to_html_node(markdown):
	blocks = markdown_to_blocks(markdown)
	children = []
	for block in blocks:
		html_node = block_to_html_node(block)
		children.append(html_node)
	return ParentNode("div", children, None)