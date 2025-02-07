#! python3
# 打开文件夹中所有的.txt文件，查找匹配用户提供的正则表达式的所有行。结果应该打印到屏幕上。
# Usage: python.exe 8.9.3.py <regex> <dir>

import os, re, sys
if len(sys.argv) == 3:
    regex = re.compile(sys.argv[1])
    dirname = sys.argv[2]
    if os.path.isdir(dirname):
        for filename in os.listdir(dirname):
            if filename.endswith('.txt'):
                file = open(filename)
                content = file.readlines()
                file.close()
                for line in content:
                    if regex.search(line):
                        print(line)
    else:
        print('The second argument is not a directory.')