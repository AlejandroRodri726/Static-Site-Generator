from htmlnode import *
from textnode import *
import re

def text_to_textnodes(text):
	node = TextNode(text, TextType.TEXT)
	new_nodes = split_nodes_image([node])
	new_nodes = split_nodes_link(new_nodes)
	new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
	new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
	new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
	return new_nodes


def text_node_to_html_node(text_node):
	textType = text_node.text_type
	
	if textType is TextType.TEXT:
		return LeafNode(None, text_node.text, None)
	if textType is TextType.BOLD:
			return LeafNode("b", text_node.text, None)
	if textType is TextType.ITALIC:
		return LeafNode("i", text_node.text, None)
	if textType is TextType.CODE:
		return LeafNode("code", text_node.text, None)
	if textType is TextType.LINK:
		return LeafNode("a", text_node.text, {"href": text_node.url})
	if textType is TextType.IMAGE:
		return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
	raise ValueError(f"Invalid text type: {textType}")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
			continue
		text = node.text
		if text.count(delimiter) % 2:
			raise Exception("Invalid Markdown Syntax: Matching closing delimiter not found.")
		text_segments = text.split(delimiter)
		for segment in text_segments:
			if(delimiter + segment + delimiter) in text:
				new_nodes.append(TextNode(segment, text_type))
				text = text.replace(delimiter + segment + delimiter, '')
			else:
				if len(segment) > 0:
					new_nodes.append(TextNode(segment, TextType.TEXT))
	return new_nodes


def split_nodes_image(old_nodes):
	new_nodes = []
	for node in old_nodes:
		matches = extract_markdown_images(node.text)
		if len(matches) == 0 or node.text_type != TextType.TEXT:
			new_nodes.append(node)
			continue
		text = node.text
		for match in matches:
			segments = text.split(f"![{match[0]}]({match[1]})", 1)
			if len(segments) != 2:
				raise ValueError("invalid markdown, image section not closed")
			if segments[0] != "":
				new_nodes.append(TextNode(segments[0], TextType.TEXT))
			new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
			text = segments[1]
		if text != "":
			new_nodes.append(TextNode(text, TextType.TEXT))
	return new_nodes


def split_nodes_link(old_nodes):
	new_nodes = []
	for node in old_nodes:
		matches = extract_markdown_links(node.text)
		if len(matches) == 0 or node.text_type != TextType.TEXT:
			new_nodes.append(node)
			continue
		text = node.text
		for match in matches:
			segments = text.split(f"[{match[0]}]({match[1]})", 1)
			if len(segments) != 2:
				raise ValueError("invalid markdown, link section not closed")
			if segments[0] != "":
				new_nodes.append(TextNode(segments[0], TextType.TEXT))
			new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
			text = segments[1]
		if text != "":
			new_nodes.append(TextNode(text, TextType.TEXT))
	return new_nodes


def extract_markdown_images(text):
	matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
	return matches

def extract_markdown_links(text):
	matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
	return matches
