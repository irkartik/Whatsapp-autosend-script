from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

target = input('Enter name of person/group you want to send message to:')

string = input('Enter your message: ')

n = int(input('Enter number of times you want your message to be sent: '))

driver = webdriver.Chrome('/home/raj/Desktop/autosend-whatsapp/chromedriver')
 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
 
x_arg = '//span[contains(@title, '+ '"' +target + '"'+ ')]'
print(x_arg)
person_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
print(person_title)
person_title.click()
inp_xpath = '//div[@class="pluggable-input-body copyable-text selectable-text"][@dir="auto"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))

for i in range(n):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)