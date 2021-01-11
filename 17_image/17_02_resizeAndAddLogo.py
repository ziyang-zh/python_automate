import os
from PIL import Image

SQUARE_FIT_SIZE=300
LOGO_FILENAME='catlogo.png'
IMAGE_FAMILY=['.png','.jpg','.gif','.bmp']

logoIm=Image.open(LOGO_FILENAME)
logoWidth,logoHeight=logoIm.size
logoIm=logoIm.resize((int(logoWidth/8),int(logoHeight/8)))
logoWidth,logoHeight=logoIm.size


os.makedirs('withLogo',exist_ok=True)
for filename in os.listdir('.'):

	if filename[-4:] not in IMAGE_FAMILY or filename==LOGO_FILENAME:
		continue

	im=Image.open(filename)
	width,height=im.size

	if width>SQUARE_FIT_SIZE and height>SQUARE_FIT_SIZE:
		if width>height:
			height=int((SQUARE_FIT_SIZE/width)*height)
			width=SQUARE_FIT_SIZE
		else:
			width=int((SQUARE_FIT_SIZE/height)*width)
			height=SQUARE_FIT_SIZE

		print('Resizing %s...' % (filename))
		im=im.resize((width,height))

	print('Adding logo to %s...' % (filename))
	im.paste(logoIm,(width-logoWidth,height-logoHeight),logoIm)

	im.save(os.path.join('withLogo',filename))