from selenium import webdriver
import time,os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import sys,logging
from selenium.webdriver.support.ui import WebDriverWait
from ml_chatbot import * 	# import ml_chatbot.py from directory
from memes import *			# import memes.py from directory you can find this on github(mine).	
data=sys.argv[1:]

sys.path.insert(0, r'E:\Python\scraping')	#this used to put your code directory from where you want to import 

def send_msg():
	count=0
	name=[] #used for scrolling...
	location=[]
	flag=False
	div=browser.find_element_by_xpath('//*[@id="pane-side"]')
	while flag==False:
		div_list=browser.find_elements_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div')
		for i in div_list:
			try:
				if i.find_element_by_xpath('./div/div/div[2]/div/div').text not in name:
					flag=False
					name.append(i.find_element_by_xpath('./div/div/div[2]/div/div').text)
					height=i.get_attribute('style').split('translateY')[1].split('p')[0][1:]
					location.append(int(height))
					count+=1
				else:
					flag=True
					print("count:",count,i.find_element_by_xpath('div/div/div[2]/div/div').text)
			except Exception as e:
				print(logging.exception(e),name[i])
		browser.execute_script("arguments[0].scrollBy(0,1728);", div)
		time.sleep(1)

	try:
		ind=name.index("Shree Hari...")
		name.pop(ind)
		location.pop(ind)
	except Exception as e:
		print(logging.exception(e))
	print(len(name),len(location))

	for i in range(len(name)):
		try:
			browser.execute_script("arguments[0].scrollTo(0,"+str(location[i])+");", div)
			div_list=browser.find_elements_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div')
			for j in div_list:
				if j.find_element_by_xpath('./div/div/div[2]/div/div').text ==name[i]:
				# if j.find_element_by_xpath('./div/div/div[2]/div/div').text ==name:
					j.find_element_by_xpath('./div/div/div[2]/div/div').click()
					# browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(".")
					browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("https://youtu.be/xnqiK6ZJcIU")
					time.sleep(1.5)
					browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("                                                                                                                                                         ")
					browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("Hey everyone, i am back with one more automation.")
					browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("                                                                                                                                                         ")
					browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("How to send message to all contact automatically & TALKING WITH CHATBOT..")
					browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("                                                                                                                                                         ")
					browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("Code is in description.Watch the video and subscribe my channel..")
					browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("                                                                                                                                                         ")
					browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("Stay home stay safe.")
					time.sleep(0.5)
					browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
					print(name[i]," : ",location[i])
					count+=1
		except Exception as e:
			print(logging.exception(e))
			print(name[i],location[i],count)
	

def talk_to_bot(name):
	# print(name)
	div=browser.find_element_by_xpath('//*[@id="pane-side"]')
	div_list=browser.find_elements_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div')
	for i in range(len(div_list)):
		try:
			iname=(div_list[i].find_element_by_xpath('./div/div/div[2]/div/div').text).lower()
			# print(iname)
			if iname==name:
				# div_list[i].find_element_by_xpath('./div/div/div[2]/div/div').text
				div_list[i].find_element_by_xpath('div/div/div[2]/div/div/span/span').click()
				time.sleep(3)
				msg_in=" "
				while(msg_in.lower() != "bye"):
					chat_list=browser.find_elements_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]/div')
					# print(chat_list)
					if ( 'message-in' in chat_list[len(chat_list)-1].get_attribute('class')):
						msg_in=chat_list[len(chat_list)-1].find_element_by_xpath('div/div/div/div/div/span/span').text
						if msg_in=='/memes':
							img=get_memes()
							browser.find_element_by_xpath("//span[@data-icon='clip']").click()
							time.sleep(1)
							browser.find_element_by_xpath("//input[@type='file']").send_keys(img)
							time.sleep(1)
							browser.find_element_by_xpath("//span[@data-icon='send-light']").click()
							time.sleep(1)
						else:
							msg_out=chat(msg_in)
							print(msg_in,msg_out)
							browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(msg_out)
							browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
			else:
				div_list[i].find_element_by_xpath('./div/div/div[2]/div/div').text
		except Exception as e:
			print(logging.exception(e))



chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
browser= webdriver.Chrome(options=chrome_options,executable_path=r"C:\Program Files\Python37\chromedriver")
browser.maximize_window()
action = ActionChains(browser)
browser.get("https://web.whatsapp.com/")
time.sleep(7)

wait = WebDriverWait(browser,10)
wait.until(lambda browser: browser.find_elements_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div'))

if __name__=='__main__':
	t=time.time()

	# talk_to_bot('nirmal_ai_test')#lowercase 
	send_msg()
	print("time taken:",(time.time()-t)/60)


