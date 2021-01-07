import PyPDF2
pdfFileObj=open('meetingminutes.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj=pdfReader.getPage(0)
#print(pageObj.extractText())

pdfReader=PyPDF2.PdfFileReader(open('encrypted.pdf','rb'))
print(pdfReader.isEncrypted)
pdfReader.decrypt('rosebud')
pageObj=pdfReader.getPage(0)

pdf1File=open('meetingminutes.pdf','rb')
pdf2File=open('meetingminutes2.pdf','rb')
pdf1Reader=PyPDF2.PdfFileReader(pdf1File)
pdf2Reader=PyPDF2.PdfFileReader(pdf2File)
pdfWriter=PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
	pageObj=pdf1Reader.getPage(pageNum)
	pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
	pageObj=pdf2Reader.getPage(pageNum)
	pdfWriter.addPage(pageObj)

pdfOutputFile=open('combinedminutes.pdf','wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()

minutesFile=open('meetingminutes.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(minutesFile)
page=pdfReader.getPage(0)
page.rotateClockwise(90)
pdfWriter=PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile=open('rotatedPage.pdf','wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()

minutesFile=open('meetingminutes.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage=pdfReader.getPage(0)
pdfWatermarkReader=PyPDF2.PdfFileReader(open('watermark.pdf','rb'))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter=PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for PageNum in range(1,pdfReader.numPages):
	pageObj=pdfReader.getPage(PageNum)
	pdfWriter.addPage(pageObj)
resultPdfFile=open('watermarkedCover.pdf','wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()

pdfFile=open('meetingminutes.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdfFile)
pdfWriter=PyPDF2.PdfFileWriter()
for pageNum in range(pdf1Reader.numPages):
	pdfWriter.addPage(pdf1Reader.getPage(pageNum))
pdfWriter.encrypt('swordfish')
resultPdf=open('encryptedminutes.pdf','wb')
pdfWriter.write(resultPdf)
resultPdf.close()
