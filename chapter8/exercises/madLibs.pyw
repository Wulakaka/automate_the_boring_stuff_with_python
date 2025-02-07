#! Python3
# madLibs.pyw - Reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
# Usage: py.exe madLibs.pyw <text file>

import sys, os, re

# print(sys.argv)

if len(sys.argv) == 2:
    isFile = os.path.isfile(sys.argv[1])
    if isFile:
        file = open(sys.argv[1])
        content = file.read()
        file.close()

        regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
        matches = regex.findall(content)

        for match in matches:
            if match == 'ADJECTIVE':
                adj = input('Enter an adjective: ')
                content = content.replace(match, adj, 1)
            elif match == 'NOUN':
                noun = input('Enter a noun: ')
                content = content.replace(match, noun, 1)
            elif match == 'ADVERB':
                adv = input('Enter an adverb: ')
                content = content.replace(match, adv, 1)
            elif match == 'VERB':
                verb = input('Enter a verb: ')
                content = content.replace(match, verb, 1)

        print(content)
        filename = input('Enter a filename to save the new text: ')
        file = open('%s.txt' % filename, 'w')
        file.write(content)
        file.close()