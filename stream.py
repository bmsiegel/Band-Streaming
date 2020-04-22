from selenium import webdriver
from seleniumrequests import Firefox
from selenium.webdriver.common.keys import Keys
import time

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

streamKey = browser.find_element_by_id('streamKey').text
print(streamKey)

browser.close()
