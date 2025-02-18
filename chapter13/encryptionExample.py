import PyPDF2, os



def filePath(name):
    list = r'D:\tmp\automate_online-materials'.split('\\')
    list.append(name)
    return os.path.sep.join(list)

pdfFile = open(filePath('meetingminutes.pdf'), 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt('swordfish')
resultPdf = open('encryptedminutes.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()