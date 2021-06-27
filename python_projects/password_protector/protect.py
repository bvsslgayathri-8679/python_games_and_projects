from PyPDF2 import PdfFileWriter , PdfFileReader
import random
pdfwriter=PdfFileWriter()

pdf=PdfFileReader('dsa.pdf')

for page_num in range(pdf.numPages):
    pdfwriter.addPage(pdf.getPage(page_num))


passw=str(random.randint(0,100))
print(passw)
pdfwriter.encrypt(passw)

with open('dsafile1.pdf','wb') as f:
    pdfwriter.write(f)
    f.close()


