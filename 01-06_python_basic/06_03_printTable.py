def printTable(data):
	colWidths=[0]*len(data)
	for i in range(len(data)):
		for j in range(len(data[i])):
			colWidths[i]=max(len(data[i][j]),colWidths[i])

	for j in range(len(data[0])):
		for i in range(len(data)):
			print(data[i][j].rjust(colWidths[i]),end=' ')
		print()

	print(colWidths)

tableData=[['apples','oranges','cherries','banana'],
		   ['Alice','Bob','Carol','David'],
		   ['dogs','cats','moose','goose']]
printTable(tableData)