import send2trash
import os 

# walks trhoug all of these file types in the path specifired
for folderName, subfolders, filenames in os.walk('C:\\code\\ATBSWP'): 
    print('The current folder is ' + folderName)

    #This list of strings of folders in the current folder 'path specified'  
    for subfolder in subfolders: 
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    # A list of strings of the files in the current folder 
    for filename in filenames: 
        print('FILE INSIDE ' + folderName + ': ' + filename)

    #this is for the space 
    print('')