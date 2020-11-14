import os

import lib.utils.constants as c

# deletes old files
def clean():
    if os.path.exists(c.filePath):
        os.remove(c.filePath)
        os.remove(c.filePath2)
    else:
        print("Can not delete the file as it doesn't exists")
