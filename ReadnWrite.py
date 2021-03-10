from pathlib import Path
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles: 
    p = (Path(r'C:\Users\Al', filename))
    print(p / 'bacon' / 'spam')
    #/ operator can be used like the + to add strings but we are using it to add variable to path 
    #Writning files 

#Output
#C:\Users\Al\accounts.txt\bacon\spam
#C:\Users\Al\details.csv\bacon\spam
#C:\Users\Al\invite.docx\bacon\spam #