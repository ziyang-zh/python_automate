from PIL import ImageColor
from PIL import Image

print(ImageColor.getcolor('red','RGBA'))
print(ImageColor.getcolor('RED','RGBA'))
print(ImageColor.getcolor('Black','RGBA'))
print(ImageColor.getcolor('chocolate','RGBA'))
print(ImageColor.getcolor('CornflowerBlue','RGBA'))

catIm=Image.open('zophie.png')
print(catIm.size)
width,height=catIm.size
print(width,height)
print(catIm.filename)
print(catIm.format)
print(catIm.format_description)
catIm.save('zophie.png')

croppedIm=catIm.crop((335,345,565,560))
croppedIm.save('cropped.png')

catCopyIm=catIm.copy()
faceIm=catIm.crop((335,345,565,560))
print(faceIm.size)
catCopyIm.paste(faceIm,(0,0))
catCopyIm.paste(faceIm,(400,500))
catCopyIm.save('paste.png')

catImWidth,catImHeight=catIm.size
faceImWidth,faceImHeight=faceIm.size
catCopyTwo=catIm.copy()
for left in range(0,catImWidth,faceImWidth):
	for top in range(0,catImHeight,faceImHeight):
		print(left,top)
		catCopyTwo.paste(faceIm,(left,top))
catCopyTwo.save('tiled.png')

width,height=catIm.size
quartersizedIm=catIm.resize((int(width/2),int(height/2)))
quartersizedIm.save('quartersized.png')
svelteIm=catIm.resize((width,height+300))
svelteIm.save('svelte.png')

catIm.rotate(90).save('rotated90.png')
catIm.rotate(180).save('rotated180.png')
catIm.rotate(270).save('rotated270.png')
catIm.rotate(6).save('rotated6.png')
catIm.rotate(6,expand=True).save('rotated6_expanded.png')

catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

im=Image.new('RGBA',(100,200),'purple')
im.save('purpleImage.png')
im2=Image.new('RGBA',(20,20))
im2.save('transparentImage.png')

im=Image.new('RGBA',(100,100))
im.getpixel((0,0))
for x in range(100):
	for y in range(50):
		im.putpixel((x,y),(210,210,210))

for x in range(100):
	for y in range(50,100):
		im.putpixel((x,y),ImageColor.getcolor('darkgray','RGBA'))
print(im.getpixel((0,0)))	
print(im.getpixel((0,50)))
im.save('putPixel.png')	

