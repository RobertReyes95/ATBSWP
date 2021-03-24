# This sciprt will allow you to read the contents of a ZIP file

import zipfile, os  
from pathlib import Path 
 
p = Path('C:\\temp')
exampleZip = zipfile.ZipFile(p / 'test.zip')
print(exampleZip.namelist())    # ['Temptest.pdf', 'InterDriver_7.4.3_M-3.exe']
print('')#for spca 

#this will print the file size of specified file
spamInfo = exampleZip.getinfo('Temptest.pdf')
print(spamInfo.file_size) # 271178 
print('')

spamInfo.compress_size # this will comrpess the file in the zip that you specifiy 

#This is dividing the orginal files size by the compresses file size to see how much it has been shrunked
totalCompress = f'Commpressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!' 
print(totalCompress)

# Extracting from a ZIP
# exampleZip.extractall('C:\\temp\\Temp')
exampleZip.close()

# Creating and adding to a ZIP File
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('test.txt', compress_type=zipfile.ZIP_DEFLATED) # the file must be in the path that you are currently working in 
newZip.close()

