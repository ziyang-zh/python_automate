import smtplib,imapclient,pprint,pyzmail
from email.header import Header
from email.mime.text import MIMEText

mailInfo={
	'from':'from@qq.com',
	'to':'to@qq.com',
	'smtp_hostname':'smtp.qq.com',
	'imap_hostname':'imap.qq.com',
	'username':'example@qq.com',
	'authorization':'xxxxxxxxxxxxxxxxx',
	'mailsubject':'Hello',
	'mailtext':'Hello world!',
	'mailcoding':'utf-8',
}

imapObj=imapclient.IMAPClient(mailInfo['imap_hostname'],ssl=True)
imapObj._MAXLINE=10000

imapObj.login(mailInfo['username'],mailInfo['authorization'])
pprint.pprint(imapObj.list_folders())

imapObj.select_folder('INBOX',readonly=False)
UIDs=imapObj.search('SINCE 01-Jan-2021')
print(UIDs)

rawMessages=imapObj.fetch(UIDs,['BODY[]'])
message=pyzmail.PyzMessage.factory(rawMessages[59][b'BODY[]'])
print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))

print(message.text_part!=None)
#print(message.text_part.get_payload().decode(message.text_part.charset))
print(message.html_part!=None)
print(message.html_part.get_payload().decode(message.html_part.charset))

#imapObj.delete_messages([61])
#imapObj.expunge()

imapObj.logout()

smtpObj=smtplib.SMTP(mailInfo['smtp_hostname'],587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(mailInfo['username'],mailInfo['authorization'])

msg=MIMEText(mailInfo['mailtext'],'html',mailInfo['mailcoding'])
msg['Subject']=Header(mailInfo["mailsubject"],mailInfo['mailcoding'])
msg['from']=mailInfo['from']
msg['to']=mailInfo['to']

smtpObj.sendmail(mailInfo['from'],mailInfo['to'],msg.as_string())
smtpObj.quit()


