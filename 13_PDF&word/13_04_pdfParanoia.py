import os,PyPDF2,send2trash

password='python'

for foldername,subfolders,filenames in os.walk('./paranoia'):
	print('The current folder is '+foldername)
	for filename in filenames:
		if filename.endswith('pdf'):
			print('Reading file "'+filename+'"...')
			filePath=os.path.join(foldername,filename)
			pdfFile=open(filePath,'rb')
			pdfReader=PyPDF2.PdfFileReader(pdfFile)

			print('Copying file "'+filename+'_encrypted...')
			pdfWriter=PyPDF2.PdfFileWriter()
			for PageNum in range(pdfReader.numPages):
				pageObj=pdfReader.getPage(PageNum)
				pdfWriter.addPage(pageObj)
			pdfWriter.encrypt(password)
			resultPdf=open(filePath[:-4]+'_encrypted.pdf','wb')
			pdfWriter.write(resultPdf)
			resultPdf.close()

			pdfReader=PyPDF2.PdfFileReader(open(filePath[:-4]+'_encrypted.pdf','rb'))
			if pdfReader.decrypt(password):
				print('Removing file "'+filename+'"...')
				send2trash.send2trash(filePath)
