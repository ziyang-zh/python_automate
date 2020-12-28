import os,re,shutil

fileRegex=re.compile(r'^.*\.(jpg|pdf)$')

for foldername,subfolders,filenames in os.walk('./unselected'):
	for filename in filenames:
		if fileRegex.search(filename):
			old_file=foldername+os.path.sep+filename
			new_file='./selected'+os.path.sep+filename
			print('copying "%s" to "%s"...' % (old_file,new_file))
			shutil.copy(old_file,new_file)
