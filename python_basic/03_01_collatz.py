def collatz(number):
	print(number)
	if number==1:
		return 1
	elif number%2==0:
		number=number//2
		return collatz(number)
	else:
		number=3*number+1
		return collatz(number)

print('Enter number: ')
#num=input()
num="3"
try:
	num=int(num)
except ValueError:
	print('Input must be an integer')
else:
	collatz(num)

