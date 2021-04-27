import glob, os, shutil
from pathlib import Path


def tree_scanner(root):
    p = Path.home()
    target = "code\test"
    for file in os.listdir(root): 
        if file.endswith(".py"):
            shutil.copy(p / file, p / target)
        else:
            break

            
    
tree_scanner("c:\code\GUI")