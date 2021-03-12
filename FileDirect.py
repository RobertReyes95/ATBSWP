from pathlib import Path 
import os

print(Path.cwd())  #Otuput = C:\code\ATBSWP
os.chdir('C:\\Windows\\System32')
print(Path.cwd()) #Output = C:\Windows\System32

#This is how you change directoy, python will throw out an error if you try to chnage dir that doens't
# exist