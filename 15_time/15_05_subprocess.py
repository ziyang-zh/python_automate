import subprocess

calcProc=subprocess.Popen('/usr/bin/gnome-calculator')
print(calcProc.poll==None)
print(calcProc.wait())
print(calcProc.poll())

fileObj=open('hello.txt','w')
fileObj.write('Hello world！')
fileObj.close()
subprocess.Popen(['see','hello.txt'],shell=True)

