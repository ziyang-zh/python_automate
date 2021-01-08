import time,pyperclip

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch')
input()
print('Started.')
startTime=time.time()
lastTime=startTime
lapNum=1

outputs=''
try:
	while True:
		input()
		lapTime=round(time.time()-lastTime,2)
		totalTime=round(time.time()-startTime,2)
		output='Lap #%s: %s (%s)'%(str(lapNum).rjust(2),str(totalTime).rjust(5),str(lapTime).rjust(5))
		print(output,end='')
		outputs+=output
		outputs+='\n'
		lapNum+=1
		lastTime=time.time()
except KeyboardInterrupt:
	pyperclip.copy(outputs)
	print('\nDone.')