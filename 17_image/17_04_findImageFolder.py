import os
from PIL import Image

IMAGE_FAMILY=['.png','.jpg','.gif','.bmp']
for foldername,subfolders,filenames in os.walk('/home/ziyang-zh'):
	if foldername[0]!='.':
		numPhotoFiles=0
		numNonPhotoFiles=0
		for filename in filenames:
			if filename[-4:] not in IMAGE_FAMILY:
				numNonPhotoFiles+=1
				continue
			try:
				im=Image.open(foldername+'/'+filename)
			except:
				pass
			width,height=im.size
			if width>500 and height>500:
				numPhotoFiles+=1
			else:
				numNonPhotoFiles+=1
		if numPhotoFiles>numNonPhotoFiles:
			print(foldername) 




