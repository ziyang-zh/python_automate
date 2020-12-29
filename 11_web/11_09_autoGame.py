from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

path=os.path.abspath('.')
broswer=webdriver.Chrome(path+'/chromedriver')
broswer.get('https://gabrielecirulli.github.io/2048/')
htmlElem=broswer.find_element_by_tag_name('html')
for i in range(100):
	htmlElem.send_keys(Keys.UP)
	htmlElem.send_keys(Keys.RIGHT)
	htmlElem.send_keys(Keys.DOWN)
	htmlElem.send_keys(Keys.LEFT)