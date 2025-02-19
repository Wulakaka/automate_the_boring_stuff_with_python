#! python3
# encryptDirPdfs.py - 使用命令行的参数加密目录及子目录的 .pdf 文件，使用 _encrypted.pdf 后缀替换原始文件。

import PyPDF2, os


def encryptDirPdfs(dirname, pwd):
    for folderName, subfolders, filenames in os.walk(dirname):
        for filename in filenames:
            if filename.endswith('.pdf'):

                file = open(os.path.join(folderName, filename), 'rb')
                pdfReader = PyPDF2.PdfFileReader(file)
                if pdfReader.isEncrypted:
                    file.close()
                    continue
                pdfWriter = PyPDF2.PdfFileWriter()
                for num in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(num))

                pdfWriter.encrypt(pwd)

                newFilename = filename.replace('.pdf', '_encrypted.pdf')
                outputFile = open(newFilename, 'wb')
                pdfWriter.write(outputFile)
                # 在 write 之前不能 close
                file.close()
                outputFile.close()
                print(newFilename)


encryptDirPdfs('D:\\tmp\\automate_online-materials', 'abc')
