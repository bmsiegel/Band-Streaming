from selenium import webdriver
from seleniumrequests import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import subprocess
import clipboard

GMF_BAND_ID = 79162159
JBS_BAND_ID = 79463189

browser = Firefox()
browser.get('https://auth.band.us/email_login')

browser.implicitly_wait(10)

textBox = browser.find_element_by_xpath('//*[@id="email_login_form"]')

textBox.find_element_by_id('input_email').send_keys('', Keys.RETURN)

time.sleep(2.5)

browser.find_element_by_id('pw').send_keys('', Keys.RETURN)

time.sleep(5)

browser.get('https://band.us/band/{}/create-live'.format(JBS_BAND_ID))

time.sleep(5)
browser.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/div/div[2]/button[1]').click()
browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div[3]/div[4]/div/button').click()

button = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div[3]/div[3]/div/button');
action = ActionChains(browser)
action.move_to_element(button);
action.perform();
time.sleep(2.5)

browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div[3]/div[3]/div/button').click()
time.sleep(2.5)
browser.switch_to.alert.accept()

streamKey = clipboard.paste()
print('Stream Key: {}'.format(streamKey))

args = ['rtmp://global-rtmp.lip2.navercorp.com:8080/relay', streamKey]
args.insert(0, './stream.sh')

print (args)
subprocess.Popen(args, cwd=os.getcwd())

browser.close()
