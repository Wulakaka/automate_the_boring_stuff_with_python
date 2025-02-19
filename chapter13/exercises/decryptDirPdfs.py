#! python3
import PyPDF2, os


def decryptDirPdfs(dirname, pwd):
    for folderName, subfolders, filenames in os.walk(dirname):
        for filename in filenames:
            if filename.endswith('.pdf'):

                file = open(os.path.join(folderName, filename), 'rb')
                pdfReader = PyPDF2.PdfFileReader(file)
                if pdfReader.isEncrypted:
                    if pdfReader.decrypt(pwd) == 1:
                        pdfWriter = PyPDF2.PdfFileWriter()
                        for num in range(pdfReader.numPages):
                            pdfWriter.addPage(pdfReader.getPage(num))
                        outputFilename = filename.replace('.pdf', '_decrypted.pdf')
                        outputFile = open(outputFilename, 'wb')
                        pdfWriter.write(outputFile)
                        outputFile.close()
                        file.close()
                    else:
                        print('file %s has not been decrypted correctly.' % filename)


decryptDirPdfs('.', 'abc')
