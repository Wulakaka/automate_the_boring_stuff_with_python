#! python3
# searchAndCopy.py - Copies all files with a certain extension in a directory to another directory.
# 选择性拷贝

import os,shutil

def searchAndCopy(fileExt, srcDir, destDir):
    destDir = os.path.abspath(destDir)
    if not os.path.exists(destDir):
        os.makedirs(destDir)
    for folderName, subfolders, filenames in os.walk(srcDir):
        if folderName == destDir:
            continue
        for filename in filenames:
            if filename.endswith(fileExt):
                path = os.path.join(folderName, filename)
                print('Copying %s to %s...' % (path, destDir))
                shutil.copy(path, destDir)

searchAndCopy('.txt', 'D:\\github', '.\\test')