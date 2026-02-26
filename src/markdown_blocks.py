from enum import Enum
import re

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