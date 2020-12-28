import random
guess=''
guess_dict={'heads':1,'tails':0}
while guess not in guess_dict.keys():
	print('Guess the coin toss! Enter heads or tails:')
	guess=input()
toss=random.randint(0,1)
if toss==guess_dict[guess]:
	print('You got it!')
else:
	guess=''
	while guess not in guess_dict.keys():
		print('Nope! Guess again!')
		guess=input()
	if toss==guess_dict[guess]:
		print('You got it!')
	else:
		print('Nope. You are really bad at this game.')