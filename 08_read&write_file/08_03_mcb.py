import shelve,pyperclip,sys
mcbShelf=shelve.open('mcb')

if len(sys.argv)==3:
	if sys.argv[1].lower()=='save':
		mcbShelf[sys.argv[2]]=pyperclip.paste()
	elif sys.argv[1].lower()=='delete':
		if sys.argv[2] in mcbShelf:
			del mcbShelf[sys.argv[2]]
elif len(sys.argv)==2:
	if sys.argv[1].lower()=='list':
		pyperclip.copy(str(list(mcbShelf.keys())))
		#print(str(list(mcbShelf.keys())))
	elif sys.argv[1].lower()=='delete':
		mcbShelf.clear()
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()