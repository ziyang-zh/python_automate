import csv
exampleFile=open('example.csv')
exampleReader=csv.reader(exampleFile)
exampleData=list(exampleReader)
print(exampleData)
print(exampleData[0][0])
print(exampleData[0][1])
exampleFile.close()

exampleFile=open('example.csv')
exampleReader=csv.reader(exampleFile)
for row in exampleReader:
	print('Row #'+str(exampleReader.line_num)+' '+str(row))
exampleFile.close()

outputFile=open('output.csv','w',newline='')
outputWriter=csv.writer(outputFile)
outputWriter.writerow(['spam','eggs','bacon','ham'])
outputWriter.writerow(['Hello world!','eggs','bacon','ham'])
outputWriter.writerow([1,2,3.141592,4])
outputFile.close()

csvFile=open('example.tsv','w',newline='')
csvWriter=csv.writer(csvFile,delimiter='\t',lineterminator='\n\n')
csvWriter.writerow(['apples','oranges','grapes'])
csvWriter.writerow(['aggs','bacon','ham'])
csvWriter.writerow(['spam','spam','spam','spam','spam','spam'])
csvFile.close()
