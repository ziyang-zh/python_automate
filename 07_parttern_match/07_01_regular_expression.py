import re

phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: '+mo.group())

phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group())
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.groups())

phoneNumRegex=re.compile(r'(\(\d\d\d\))(\d\d\d-\d\d\d\d)')
mo=phoneNumRegex.search('My number is (415)555-4242.')
print(mo.groups())

heroRegex=re.compile(r'Batman|Tina Fey')
mo1=heroRegex.search('Batman and Tina Fey')
mo2=heroRegex.search('Tina Fey and Batman')
print(mo1.group(),mo2.group())

batRegex=re.compile(r'Bat(man|mobile|copter|bat)')
mo=batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))


batRegex=re.compile(r'Bat(wo)?man')
mo1=batRegex.search('The Adventures of Batman')
mo2=batRegex.search('The Adventures of Batwoman')
print(mo1.group(),mo2.group())

phoneNumRegex=re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1=phoneNumRegex.search('My number is 415-555-4242.')
mo2=phoneNumRegex.search('My number is 555-4242.')
print(mo1.group(),mo2.group())

batRegex=re.compile(r'Bat(wo)*man')
mo1=batRegex.search('The Adventures of Batman')
mo2=batRegex.search('The Adventures of Batwoman')
mo3=batRegex.search('The Adventures of Batwowowowowoman')
print(mo1.group(),mo2.group(),mo3.group())

batRegex=re.compile(r'Bat(wo)+man')
mo1=batRegex.search('The Adventures of Batman')
mo2=batRegex.search('The Adventures of Batwoman')
mo3=batRegex.search('The Adventures of Batwowowowowoman')
print(mo1,mo2.group(),mo3.group())

haRegex=re.compile(r'(Ha){3}')
mo1=haRegex.search('HaHaHa')
mo2=haRegex.search('Ha')
print(mo1.group(),mo2)

greedyHaRegex=re.compile(r'(Ha){3,5}')
nongreedyHaRegex=re.compile(r'(Ha){3,5}?')
mo1=greedyHaRegex.search('HaHaHaHaHa')
mo2=nongreedyHaRegex.search('HaHaHaHaHa')
print(mo1.group(),mo2.group())

phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneNumRegex.findall('Cell: 415-555-9999 Work: 2112-555-0000')
print(mo)

phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo=phoneNumRegex.findall('Cell: 415-555-9999 Work: 2112-555-0000')
print(mo)

xmasRegex=re.compile(r'\d+\s+\w+')
mo=xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladys, \
						8 maids, 7 swans, 6geese, 5 rings, \
						4 birds, 3 hens, 2 doves, 1 partridge')
print(mo)

vowelRegex=re.compile(r'[aeiouAEIOU]')
mo=vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

vowelRegex=re.compile(r'[^aeiouAEIOU]')
mo=vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

beginsWithHello=re.compile(r'^Hello')
mo1=beginsWithHello.search('Hello World!')
mo2=beginsWithHello.search('He said hello.')
print(mo1,mo2)

endsWithNumber=re.compile(r'\d$')
mo1=endsWithNumber.search('Your number is 42')
mo2=endsWithNumber.search('Your number is forty two.')
print(mo1,mo2)

wholeStringIsNum=re.compile(r'^\d+$')
mo1=wholeStringIsNum.search('1234567890')
mo2=wholeStringIsNum.search('12345xyz67890')
mo3=wholeStringIsNum.search('123 4567890')
print(mo1,mo2,mo3)

atRegex=re.compile(r'.at')
mo=atRegex.findall('The cat in the hat sat on the flat mat')
print(mo)

nameRegex=re.compile(r'First Name: (.*) Last Name: (.*)')
mo=nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1),mo.group(2))

nongreedyRegex=re.compile(r'<.*?>')
greedyRegex=re.compile(r'<.*>')
mo1=nongreedyRegex.search('<To serve man> for dinner.>')
mo2=greedyRegex.search('<To serve man> for dinner.>')
print(mo1.group(),mo2.group())

noNewlineRegex=re.compile('.*')
newlineRegex=re.compile('.*',re.DOTALL)
mo1=noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
mo2=newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo1.group())
print(mo2.group())

robocop=re.compile(r'robocop',re.I)
mo1=robocop.search('RoboCop is part man, part machine, all cop')
mo2=robocop.search('ROBOCOP protects the innocent.')
mo3=robocop.search('Al, why dose your programming book talk about robocop so much?')
print(mo1.group(),mo2.group(),mo3.group())

namesRegex=re.compile(r'Agent \w+')
mo=namesRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob')
print(mo)

agentNamesRegex=re.compile(r'Agent (\w)\w+')
mo=agentNamesRegex.sub(r'\1****','Agent Alice told Agent Corol that Agent Eve knew Agent Bob was a double Agent.')
print(mo)

phoneRegex=re.compile(r'''(
	(\d{3}|\(\d{3}\))?			#area code
	(\s|-|\.)?					#separator
	\d{3}						#first 3 digits
	(\s|-|\.)					#separator
	\d{4}						#last 4 digits
	(\s*(ext|x|ext.)\s*\d{2,5})?#extension
	)''',re.VERBOSE)

someRegexValue=re.compile('foo',re.IGNORECASE|re.DOTALL)
someRegexValue=re.compile('foo',re.IGNORECASE|re.DOTALL|re.VERBOSE)




