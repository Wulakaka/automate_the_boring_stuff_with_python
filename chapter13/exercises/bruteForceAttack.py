import re, PyPDF2


def main(filename):
    pdfFileReader = PyPDF2.PdfFileReader(open(filename, 'rb'))
    regex = re.compile(r'(.*)\n')
    content = open('./dictionary.txt').readlines()
    for name in content:
        result = regex.match(name)
        if result:
            name = result[1]
        encryptResult = pdfFileReader.decrypt(name)
        if encryptResult == 1:
            print(name)
            return
        name = name.lower()
        encryptResult = pdfFileReader.decrypt(name)
        if encryptResult == 1:
            print(name)
            return


main('test.pdf')
