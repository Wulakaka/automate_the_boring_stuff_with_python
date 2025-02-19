# This script runs on Windows only, and you must have Word installed.
import win32com.client
import docx
wordFilename = 'test.docx'
pdfFilename = 'test.pdf'

doc = docx.Document()
# Code to create Word document goes here.
doc.save(wordFilename)

wdFormatPDF = 17 # Word's numeric code for PDFs.
wordObj = win32com.client.Dispatch('Word.Application')

docObj = wordObj.Documents.Open(wordFilename)
docObj.SaveAs(pdfFilename, FileFormat=wdFormatPDF)

docObj.close()
wordObj.quit()
