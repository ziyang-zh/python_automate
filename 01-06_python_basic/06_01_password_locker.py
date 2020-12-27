import sys,pyperclip

passwords={
	'email':'thisismyemailpassword',
	'blog':'myblogpassword',
 	'luggage':'12345'
}

if len(sys.argv)<2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()

account=sys.argv[1]

if account in passwords:
	pyperclip.copy(passwords[account])
	print('Password for '+account+' copied to clipbord.')
else:
	print('There is no account named '+account)
