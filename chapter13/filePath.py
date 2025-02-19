#! python3
import os

def filePath(name):
    list = r'D:\tmp\automate_online-materials'.split('\\')
    list.append(name)
    return os.path.sep.join(list)