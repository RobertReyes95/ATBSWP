from pathlib import Path 
import os

#print(Path.cwd())  #Otuput = C:\code\ATBSWP
os.chdir('C:\\Windows\\System32')
#print(Path.cwd()) #Output = C:\Windows\System32

#This is how you change directoy, python will throw out an error if you try to chnage dir that doens't
# exist

Path.cwd().is_absolute() #Returns True if path is absolute


Path('my/relative/path')# Example of getting a abosulte path from a relative path  
Path.cwd() / Path('my/relative/path') 

Path.home() / Path('my/relative/path') #gets an absoulte path using the home directoy instead of the corrent wokring dic

#How to extrat the drive attribute
p = Path('C:/users/Al/spam.txt')
p.anchor

#Extracting other attributes
p.parent #C:\users\Al
p.name #spam.txt
p.stem #spam
p.suffix #.txt
p.drive #C:
