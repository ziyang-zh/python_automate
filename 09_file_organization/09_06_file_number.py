import os,re,shutil

fileDir='./filelist_random'
fileList=os.listdir(fileDir)
fileList.sort()
fileNum=len(fileList)

numberRegex=re.compile(r'(\d+)')

for i in range(fileNum):
	oldFilename=fileList[i]
	oldNumber=numberRegex.search(oldFilename).group(1)
	newNumber='0'*(len(oldNumber)-len(str(i)))+str(i+1)
	newFilename=numberRegex.sub(newNumber,oldFilename)
	print('updating "%s" to "%s"...' % (oldFilename,newFilename))
	shutil.copy(fileDir+os.path.sep+oldFilename,'./filelist_numbered'+os.path.sep+newFilename)
