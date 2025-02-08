#! python3
# 消除缺失的编号
# 9.8.3

import os, re, shutil


def removeMissingNumbers(dirname, prefix):
    regex = re.compile('^' + prefix + r'(\d{3}).txt$')
    filenames = os.listdir(dirname)
    numbers = []
    for filename in filenames:
        result = regex.search(filename)
        if result is not None:
            numbers.append(int(result.group(1)))

    numbers.sort()
    for i in range(len(numbers)):
        if numbers[i] != i + 1:
            newName = prefix + str(i + 1).zfill(3) + '.txt'
            oldName = prefix + str(numbers[i]).zfill(3) + '.txt'
            shutil.move(os.path.join(dirname, oldName), os.path.join(dirname, newName))


removeMissingNumbers('./test', 'test')
