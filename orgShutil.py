import shutil, os
from pathlib import Path


p = Path.home() # point ot the home directory of the pc/account your in 

# This code copies the file spam.txt to folder 'some_folder'
# shutil.copy(p / 'spam.txt', p / 'some_folder')


# Moves tst.txt and renames the file to tst2.txt
# shutil.copy(p / 'tst.txt', p / 'some_folder/tst2.txt')
s

# This code move test.txt to file the 2nd listed file directory 'Downloads'
# shutil.move('C:\\Users\\robertreyes\\Documents\\test.txt', 'C:\\Users\\robertreyes\\Downloads')

# This deletes .rxt files from path 
for filename in Path.home().glob('*.rxt'): 
    #os.unlink(filename)
    print(filename) # print file before deleting if you want to make sure


