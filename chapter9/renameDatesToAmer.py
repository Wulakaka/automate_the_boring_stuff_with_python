#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?) # all text before the date
    (([0123])?\d)-                 # one or two digits for the day
    (([01])?\d)-                     # one or two digits for the month
    ((19|20)\d\d)                   # four digits for the year
    (.*?)$                          # all text after the date
    """, re.VERBOSE)

# Loop over the files in the working directory.
for euroFilename in os.listdir('./test'):
    mo = datePattern.search(euroFilename)

    # Skip files without a date.
    if mo is None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    dayPart = mo.group(2)
    monthPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the American-style filename.
    amerFilename = beforePart + monthPart + '-' + dayPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('./test')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print('Renaming "%s" to "%s"...' % (euroFilename, amerFilename))
    shutil.move(euroFilename, amerFilename) # uncomment after testing