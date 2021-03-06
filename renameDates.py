# This is a project idea fro renaming Files with the american style dates to european style dates 

import shutil, os, re 

# Creates a regex that matches fiels with the American date format
datePattern = re.compile(r"""^(.*?)# all text before the date
    ((0|1)?\d)                      # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day 
    ((19|20)d\d)                    # four digits for the year
    (.*?)$                          # all text after the date
    """, re.VERBOSE) 

# Loop over the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    #Skip files without a date
    if mo == None: 
        continue

    # Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)
    
    
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    #Get the full, absolute file paths 
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    #Rename the Files. 

    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    shutil.move(amerFilename ,euroFilename)





