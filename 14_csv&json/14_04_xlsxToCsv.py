import os,openpyxl,csv

os.makedirs('csvSpreadsheets',exist_ok=True)
for excelFile in os.listdir('./excelSpreadsheets'):
	wb=openpyxl.load_workbook('./excelSpreadsheets/'+excelFile)
	for sheetname in wb.sheetnames:
		sheet=wb[sheetname]
		
		fileName=excelFile[:-5]+'_'+sheetname+'.csv'
		csvFile=open('./csvSpreadsheets/'+fileName,'w',newline='')
		csvWriter=csv.writer(csvFile)

		for rowNum in range(1,sheet.max_row+1):
			rowData=[]
			for colNum in range(1,sheet.max_column+1):
				rowData.append(sheet.cell(rowNum,colNum).value)
			
			csvWriter.writerow(rowData)
		csvFile.close()
