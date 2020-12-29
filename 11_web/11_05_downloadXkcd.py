import requests,os,bs4

url='https://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
filenum=10
while not url.endswith('#') and filenum:
	print('Downloading page %s...' % url)
	res=requests.get(url)
	res.raise_for_status()

	soup=bs4.BeautifulSoup(res.text,features="lxml")
	
	comicElems=soup.select('#comic img')
	if comicElems==[]:
		print('Could not find comic img.')
	else:
		comicUrl='https:'+comicElems[0].get('src')
		print('Downloading image %s...' % (comicUrl))
		res=requests.get(comicUrl)
		res.raise_for_status()

		imageFile=open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()
		filenum-=1

		prevLink=soup.select('a[rel="prev"]')[0]
		url='https://xkcd.com'+prevLink.get('href')