import json
stringhOfJsonData='{"name":"Zophie","isCat":true,"miceCaught":0,"felineIQ":null}'
jsonDataAsPythonValue=json.loads(stringhOfJsonData)
print(jsonDataAsPythonValue)

pythonValue={'isCat':True,'miceCaught':0,'name':'Zophie','felineIQ':None}
stringhOfJsonData=json.dumps(pythonValue)
print(stringhOfJsonData)