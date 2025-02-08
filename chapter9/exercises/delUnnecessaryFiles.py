#! python3
# 删除不必要的文件
# 9.8.2
# Usage: python.exe delUnnecessaryFiles.py <dir>
import os, sys


def delUnnecessaryFiles(dirname):
    limit = 100.0
    if os.path.isdir(dirname):
        for folderName, subfolders, filenames in os.walk(dirname):
            folderSize = 0
            for filename in filenames:
                filePath = os.path.join(folderName, filename)
                size = os.path.getsize(filePath)
                size /= 1024 * 1024
                folderSize += size
                if size > limit:
                    print('The size of %s is %.2f MB.' % (filePath, size))

            if folderSize > limit:
                print('The size of %s is %.2f MB.' % (folderName, folderSize))
    else:
        print('The argument is not a directory.')


delUnnecessaryFiles('D:\\迅雷下载')
