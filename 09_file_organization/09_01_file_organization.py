import os,shutil,send2trash,zipfile

shutil.copy('./bacon/bacon.txt','./bacon/bacon_copy.txt')
shutil.move('./bacon/bacon_copy.txt','./bacon_move.txt')
shutil.move('./bacon_move.txt','./bacon.txt')
for filename in os.listdir():
	if filename.endswith('.txt'):
		os.unlink(filename)
		print(filename)
shutil.copytree('./bacon','./bacon_copy')
shutil.rmtree('./bacon_copy')

baconFile=open('bacon.txt','a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('bacon.txt')

for foldername,subfolders,filenames in os.walk('./'):
	print('The current folder is '+foldername)

	for subfolder in subfolders:
		print('SUBFOLDER OF '+foldername+': '+subfolder)
	for filename in filenames:
		print('FILE INSIDE '+foldername+': '+filename)

	print('')

exampleZip=zipfile.ZipFile('example.zip')
print(exampleZip.namelist())
spamInfo=exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print('compressed file is %sx smaller' % (round(spamInfo.file_size/spamInfo.compress_size,2)))

exampleZip.extractall()
exampleZip.extract('spam.txt','./spam_ex')

exampleZip.close()
newZip=zipfile.ZipFile('new.zip','w')
newZip.write('spam.txt',compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

os.unlink('spam.txt')
os.unlink('new.zip')
shutil.rmtree('./cats')
shutil.rmtree('./spam_ex')
