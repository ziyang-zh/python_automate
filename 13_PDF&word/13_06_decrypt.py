import PyPDF2

pdfFile=open('encryptedminutes.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdfFile)
print(pdfReader.isEncrypted)
with open('dictionary.txt','r') as passwords:
	for password in passwords.readlines():
		if pdfReader.decrypt(password.strip().lower()):
			print("password: "+password.strip().lower())
			print("done!")
			break