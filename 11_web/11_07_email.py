import os
from time import *
from selenium import webdriver

username='123456'
password='123456'
receiver='123456@qq.com'

path=os.path.abspath('.')
broswer=webdriver.Chrome(path+'/chromedriver')

broswer.get('https://mail.qq.com/')
loginFrame=broswer.find_element_by_id("login_frame")
broswer.switch_to.frame(loginFrame)
broswer.find_element_by_id("u").send_keys(username)
broswer.find_element_by_id("p").send_keys(password)
broswer.find_element_by_id("login_button").click()
sleep(1)
broswer.find_element_by_id("composebtn").click()
sleep(1)
broswer.switch_to.frame("mainFrame")
broswer.find_element_by_xpath("//*[@id='toAreaCtrl']/div/input").send_keys(receiver)
broswer.find_element_by_id("subject").send_keys("Hello")
iFrame=broswer.find_element_by_tag_name("iframe")
broswer.switch_to.frame(iFrame)
#editerFrame=broswer.find_element_by_class_name("qmEditorIfrmEditArea")
#broswer.switch_to.frame(editerFrame)
broswer.find_element_by_tag_name("body").send_keys("Hello World!")
broswer.switch_to.parent_frame()
broswer.find_element_by_link_text("发送").click()
