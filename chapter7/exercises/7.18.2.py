import re


def main(s, r=None):
    stripResult = s.strip(r)

    if r is None:
        r = r'\s'
    regexStart = re.compile(r'^[' + r + r']*')
    regexEnd = re.compile(r'[' + r + r']*$')
    result = regexEnd.sub('', regexStart.sub('', s))
    print(stripResult == result)
    return regexEnd.sub('', regexStart.sub('', s))


print(main('  adfs  \t'))
print(main('  ad   fs  \t'))
print(main('    '))
print(main('  adfs  ', 'f'))
print(main('  adfs  ', 'bf'))
