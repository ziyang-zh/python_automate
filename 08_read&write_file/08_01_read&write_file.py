import os,shelve,pprint
import myCats

print(os.path.join('usr','bin','spam'))

myFiles=['accounts.txt','details.csv','invite.docx']
for filename in myFiles:
	print(os.path.join('/home/ziyang-zh/python_automate',filename))

print(os.getcwd())
#os.chdir('/home/ziyang-zh/')
#print(os.getcwd())
#os.makedirs('makedir')
print(os.path.abspath('.'))
print(os.path.abspath('./makedir'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

print(os.path.relpath('/home/ziyang-zh/'))
print(os.path.relpath('/home/ziyang-zh/','/home'))

path='/home/ziyang-zh/python_automate/08_01_read&write_file.py'
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.split(path))
print(path.split(os.path.sep))

print(os.path.getsize('/home/ziyang-zh/'))
print(os.listdir('/home/ziyang-zh/'))
totalSize=0
for filename in os.listdir('/home/ziyang-zh/'):
	totalSize=totalSize+os.path.getsize(os.path.join('/home/ziyang-zh/',filename))
print(totalSize)

print(os.path.exists('/home/ziyang-zh/'))
print(os.path.exists('/home/ziyang-zh/no_this_dir/'))
print(os.path.isdir('/home/ziyang-zh/'))
print(os.path.isfile('/home/ziyang-zh/'))

helloFile=open('./hello.txt')
print(helloFile.read())
helloFile.close()

helloFile=open('./hello.txt')
print(helloFile.readlines())
helloFile.close()

baconFile=open('bacon.txt','w')
print(baconFile.write('Hello World!\n'))
baconFile.close()
baconFile=open('bacon.txt','a')
print(baconFile.write('Bacon is not a vegetable.'))
baconFile.close()
baconFile=open('bacon.txt')
content=baconFile.read()
baconFile.close()
print(content)

shelfFile=shelve.open('mydata')
cats=['Zophie','pooka','Simon']
shelfFile['cats']=cats
shelfFile.close()

shelfFile=shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()

shelfFile=shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

cats=[{'name':'Zophie','desc':'chubby'},\
		{'name':'Pooka','desc':'fluffy'}]
print(pprint.pformat(cats))
fileObj=open('myCats.py','w')
print(fileObj.write('cats = '+pprint.pformat(cats)+'\n'))
fileObj.close()

print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])