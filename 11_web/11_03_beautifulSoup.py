import requests,bs4


exampleFile=open('example.html')
#exampleSoup=bs4.BeautifulSoup(exampleFile,features="lxml")
exampleSoup=bs4.BeautifulSoup(exampleFile.read(),features="lxml")
print(type(exampleSoup))
elems=exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

pElems=exampleSoup.select('p')
print(str(pElems[0]))
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[2]))
print(pElems[2].getText())

spanElem=exampleSoup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_noneexistent_addr')==None)
print(spanElem.attrs)