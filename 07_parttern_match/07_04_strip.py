import re

def strip(string):
	spaceRegex=re.compile(r'^(\s+)?(.*)(\s+)?$')
	mo=spaceRegex.search(string)
	return mo.group(2)

string1='abcdefg'
string2=' abcdefg'
string3='abcdefg '
string4=' abcdefg '
string5='\n abcdefg\t '

print(strip(string1))
print(strip(string2))
print(strip(string3))
print(strip(string4))
print(strip(string5))

