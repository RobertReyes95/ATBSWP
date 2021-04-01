import zipfile, os 

def backupToZip(folder): 
    #back up the entire contents of "Folder" into a ZIP file

    folder = os.path.abspath(folder) # make sure folder is absolute

    # Figure out the filename this code should use based on what fiels already exist 
    number = 1
    while True: 
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # TODO Creat the ZIP File 

    # TODO: Walk the entire folder tree and compress the files in each folder

    print("Done.")

backupToZip('C:\\delicious')

