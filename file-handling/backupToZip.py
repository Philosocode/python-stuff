import zipfile
import os


# folder = string path to the folder.
def backupToZip(folder):
    # Backup the entire content of 'folder' into a ZIP file.
    folder = os.path.abspath(folder)    # Make sure the folder is absolute

    # Figure out the filename based on what files exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    # Create ZIP file
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress files in each folder...
    for foldername, subfolders, filename in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add current folder to ZIP file
        backupZip.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase / os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip')
                continue  # Don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
        backupZip.close()
        print('Done.')


backupToZip('C:\\delicious')
