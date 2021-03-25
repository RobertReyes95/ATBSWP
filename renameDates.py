# This is a project idea fro renaming Files with the american style dates to european style dates 

import shutil, os, re 

# Creates a regex that matches fiels with the American date format
datePatteren = re.compile(r"""^(.*?)# all text before the date
    (( 0|1)?\d)                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day 
    ((19|20)d\d)                    # four digits for the year
    (.*?)$                          # all text after the date
    """, re.VERBOSE) 
