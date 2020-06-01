from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

ORG_NAME = "mobile-developers-of-berkeley" #www.linkedin.com/company/ORG_NAME
EMAIL = "" 
PASSWORD = ""
MESSAGE = 'Hi, we are in the same organization and I would like to connect with you!'


driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.linkedin.com/uas/login?")
time.sleep(1 + random.random())
driver.find_element_by_id('username').send_keys(EMAIL)
driver.find_element_by_id('password').send_keys(PASSWORD)
driver.find_element_by_xpath("//button[contains(text(), 'Sign in')]").click()
time.sleep(2 + 3 * random.random())


driver.get("https://www.linkedin.com/company/" + ORG_NAME)
time.sleep(2*random.random())
try:
    driver.find_element_by_partial_link_text("See all").click()
except:
    print("Message popup blocking the script, go on settings and turn off automatically open messages")

time.sleep(2 + 3 * random.random())
#### IF YOU ONLY WANT TO CONNECT WITH THE 2ND CONNECTIONS###
driver.get(driver.current_url + """&facetNetwork=%5B"S"%5D""")

time.sleep(2 + 3 * random.random())
connectbtns = driver.find_elements_by_class_name('search-result__action-button')

for connect in connectbtns:
    time.sleep(2*random.random())
    connect.click()

    time.sleep(random.random())
    driver.find_element_by_class_name('mr1').click()

    time.sleep(random.random())
    driver.find_element_by_name('message').send_keys(MESSAGE)

    time.sleep(random.random())
    driver.find_element_by_class_name('ml1').click()
