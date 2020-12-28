import re

with open('./libs.txt','r') as libs:
	lib=libs.read()

adjective=input("Enter an adjective:\n")
noun1=input("Enter an noun:\n")
verb=input("Enter an verb:\n")		
noun2=input("Enter an noun:\n")		
#adjective='silly'
#noun1='chandelier'
#verb='screamed'
#noun2='pickup truck'

adjectiveRegex=re.compile(r'ADJECTIVE')
noun1Regex=re.compile(r'NOUN')
verbRegex=re.compile(r'VERB')
noun2Regex=re.compile(r'NOUN')

lib=adjectiveRegex.sub(adjective,lib)
lib=noun1Regex.sub(noun1,lib,1)
lib=verbRegex.sub(verb,lib)
lib=noun2Regex.sub(noun2,lib)

with open('mad_libs.txt','w') as mad_libs:
	mad_libs.write(lib)

print(lib)