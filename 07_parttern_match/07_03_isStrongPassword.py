import re

def isStrongPassword(password):
	lenRegex=re.compile(r'^.{8,}$')
	upperRegex=re.compile(r'[A-Z]')
	lowerRegex=re.compile(r'[a-z]')
	numberRegex=re.compile(r'[0-9]')

	mo1=lenRegex.search(password)
	mo2=upperRegex.search(password)
	mo3=lowerRegex.search(password)
	mo4=numberRegex.search(password)
	return bool(mo1 and mo2 and mo3 and mo4)

mypassword1='123456'
mypassword2='ABC123'
mypassword3='ABC123456789'
mypassword4='ABCabc123456789'

print(isStrongPassword(mypassword1))
print(isStrongPassword(mypassword2))
print(isStrongPassword(mypassword3))
print(isStrongPassword(mypassword4))
