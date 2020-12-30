import openpyxl,pprint
print('Opening workbook...')
wb=openpyxl.load_workbook('censuspopdata.xlsx')
sheet=wb['Population by Census Tract']
countydata={}

print('Reading rows...')
for row in range(2,sheet.max_row+1):
	state=sheet['B'+str(row)].value
	county=sheet['C'+str(row)].value
	pop=sheet['D'+str(row)].value

	countydata.setdefault(state,{})
	countydata[state].setdefault(county,{'tracts':0,'pop':0})

	countydata[state][county]['tracts']+=1
	countydata[state][county]['pop']+=int(pop)

print('Writing results...')
resultFile=open('census2010.py','w')
resultFile.write('allData = '+pprint.pformat(countydata))
resultFile.close()
print('done')