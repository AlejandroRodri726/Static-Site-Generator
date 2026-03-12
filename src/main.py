from textnode import *
from copystatic import *
from page_generation import *

def main():
    src_path = "./static"
    dst_path = "./public"
    if os.path.isdir(dst_path):
        shutil.rmtree(dst_path)
    copy_contents(src_path, dst_path)
    generate_page("./content/index.md", "./template.html", "./public/index.html")


main()