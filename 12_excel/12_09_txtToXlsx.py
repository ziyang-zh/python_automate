import openpyxl

wb=openpyxl.Workbook()
sheet=wb['Sheet']
flag=1
with open('fruit.txt','r') as file:
	for line in file.readlines():
		sheet.cell(row=flag,column=1).value=line.strip()
		flag+=1

wb.save('fruit.xlsx')