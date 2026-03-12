from markdown_blocks import *
import os

def extract_title(markdown):
    if markdown.startswith("#"):
        title = markdown.split("\n", 1)[0]
        return title[1:].strip()
    raise Exception("No title found.")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md_file = open(from_path)
    markdown = md_file.read()
    md_file.close()

    tem_file = open(template_path)
    template = tem_file.read()
    tem_file.close()    

    node = markdown_to_html_node(markdown)
    html = node.to_html()
    title = extract_title(markdown)
    html_page = template.replace("{{ Title }}", title)
    html_page = html_page.replace("{{ Content }}", html)

    dir = os.path.dirname(dest_path)
    if not os.path.exists(dir):
        os.makedirs(dir)
    index_file = open(dest_path, 'w')
    index_file.write(html_page)
    index_file.close()