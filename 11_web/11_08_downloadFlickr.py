import requests,os,bs4

key='world'
url='https://blog.flickr.net/en/?s='
os.makedirs('flickr',exist_ok=True)

res=requests.get(url+key)
res.raise_for_status()

soup=bs4.BeautifulSoup(res.text,features="lxml")

imageElems=soup.select('img')
for i in range(len(imageElems)-1):
	if imageElems==[]:
		print('Could not find image.')
	else:
		imageUrl=imageElems[i].get('src')
		res=requests.get(imageUrl)
		try:
			res.raise_for_status()
		except:
			continue

		print('Downloading image %s...' % (imageUrl))
		imageFile=open(os.path.join('flickr',os.path.basename(imageUrl)),'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()