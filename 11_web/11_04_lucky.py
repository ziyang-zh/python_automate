import sys,requests,webbrowser,bs4
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",}

print('Searching...')
res=requests.get('https://www.baidu.com/s?wd='+' '.join(sys.argv[1:]),headers=headers)
res.raise_for_status()

soup=bs4.BeautifulSoup(res.text,features="lxml")
linkElems=soup.select('a')

opend=[]
for linkElem in linkElems:
	href=linkElem.get('href')
	if 'link?url'in str(href) and str(href) not in opend:
		opend.append(str(href))
		webbrowser.open(href)
		if len(opend)>=5 or len(opend)==len(linkElems):
			break
