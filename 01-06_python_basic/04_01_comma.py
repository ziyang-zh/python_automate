def comma_linker(alist):
	astring=''
	if len(alist)==0:
		return astring
	elif len(alist)==1:
		astring+=str(alist[0])
		return astring
	else:
		for i in range(len(alist)-1):
			astring+=str(alist[i])+", "
		astring+="and "+str(alist[-1])+"."
		return astring

spam=['apples','bananas','tofu','cats']
print(comma_linker(spam))