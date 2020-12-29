from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

path=os.path.abspath('.')
broswer=webdriver.Chrome(path+'/chromedriver')
print(type(broswer))

broswer.get('http://inventwithpython.com')
try:
	elem=broswer.find_element_by_class_name('bookcover')
	print('found <%s> element with that class name!' % (elem.tag_name))
except:
	print('Was not able to find an element with that name.')

linkElem=broswer.find_element_by_link_text('Automate the Boring Stuff with Python')
print(type(linkElem))
linkElem.click()

username='12345678'
password='12345678'

broswer.get('https://mail.qq.com/')
loginFrame=broswer.find_element_by_id("login_frame")
broswer.switch_to.frame(loginFrame)

broswer.find_element_by_id("u").send_keys(username)
broswer.find_element_by_id("p").send_keys(password)
broswer.find_element_by_id("login_button").click()

broswer.get('http://nostarch.com')
htmlElem=broswer.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)
htmlElem.send_keys(Keys.HOME)
