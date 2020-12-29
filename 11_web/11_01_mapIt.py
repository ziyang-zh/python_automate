import sys,pyperclip,webbrowser
webbrowser.open('http://inventwithpython.com/')

if len(sys.argv)>1:
	address=' '.join(sys.argv[1:])
else:
	address=pyperclip.paste()

#webbrowser.open('https://www.google.com/maps/place/'+address)
webbrowser.open('https://map.baidu.com/poi/'+address)
#汉口江滩