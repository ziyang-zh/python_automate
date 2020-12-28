import os,re

#userRegex=re.compile(input("please input a regular expression：\n"))
userRegex=re.compile('.*New York.*')

txtRegex=re.compile(r'.*.txt$')
for filename in os.listdir('./quizs/'):
	isTxt=txtRegex.search(filename)
	if isTxt:
		with open('./quizs/'+filename,'r') as fileObj:
			for line in fileObj.readlines():
				if userRegex.search(line):
					print(line)