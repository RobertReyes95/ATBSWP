import shutil, os
from pathlib import Path


p = Path.home() # point ot the home directory of the pc/account your in 

# This code copies the file spam.txt to folder 'some_folder'
# shutil.copy(p / 'spam.txt', p / 'some_folder')


# Moves tst.txt and renames the file to tst2.txt
# shutil.copy(p / 'tst.txt', p / 'some_folder/tst2.txt')


# This code move test.txt to file the 2nd listed file directory 'Downloads'
# shutil.move('C:\\Users\\robertreyes\\Documents\\test.txt', 'C:\\Users\\robertreyes\\Downloads')

# This deletes .rxt files from path 
for filename in Path.home().glob('*.rxt'): 
    #os.unlink(filename)
    print(filename) # print file before deleting if you want to make sure


#This module is used to deletes files and folders
# It is mush safer than python regular delete functions 
# becuase this will send your delted files to the recycle bin instead of perm del them 

import send2trash
baconFile = open('bacon.txt', 'a') # creates the file 
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

send2trash.send2trash('bacon.txt')

# in gefneral us send2trash.send2trash to delete files just in case you need to back the files up again 
# otherwise use shutil to permently delete files and free up disk spaces
