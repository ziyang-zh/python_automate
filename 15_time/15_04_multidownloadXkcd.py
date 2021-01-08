import requests,os,bs4,threading

os.makedirs('xkcd',exist_ok=True)

def downloadXkcd(startComic,endComic):
	for urlNumber in range(startComic,endComic):
		print('Downloading page https://xkcd.com/%s...' % (urlNumber))
		res=requests.get('https://xkcd.com/%s' % (urlNumber))
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

downloadThreads=[]
for i in range(1,12,2):
	downloadThread=threading.Thread(target=downloadXkcd,args=(i,i+2))
	downloadThreads.append(downloadThread)
	downloadThread.start()

for downloadThread in downloadThreads:
	downloadThread.join()
print('Done.')