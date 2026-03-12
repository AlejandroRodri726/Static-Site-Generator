import os
import shutil

def copy_contents(src_dir_path, dst_dir_path, log=False):
    if not os.path.exists(dst_dir_path):
        os.mkdir(dst_dir_path)
    files = os.listdir(src_dir_path) 
    for filename in files:
        path = os.path.join(src_dir_path, filename)
        if log:
            print(f"Copying {path}")

        if os.path.isfile(path):
            shutil.copy(path, dst_dir_path)
        else:
            dst_path = os.path.join(dst_dir_path, filename)
            copy_contents(path, dst_path)
    
