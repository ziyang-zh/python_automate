import os,re,send2trash

for foldername,subfolders,filenames in os.walk('./unselected'):
	for filename in filenames:
		filePath=foldername+os.path.sep+filename
		fileSize=os.path.getsize(filePath)
		if fileSize>=100000:
			print('removing "%s" (%sk) to trash...' % (filePath,fileSize))
			#send2trash.send2trash(filePath)
