from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import os
import pyperclip

url = "https://naver.com"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)

# 네이버 로그인 버튼 클릭
driver.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW").click()
time.sleep(2)

# 네이버 아이디, 패스워드
naver_id = 'seongeun0'
naver_pw = os.environ.get('naver_password')

# 네이버 아이디 입력
# driver.find_element(By.ID, 'id').send_keys(naver_id)
id_input = driver.find_element(By.ID, 'id')
pyperclip.copy(naver_id) # control + c
id_input.click() 
id_input.send_keys(Keys.COMMAND, 'v') # control + v
time.sleep(2)

# 네이버 패스워드 입력
# driver.find_element(By.ID, 'pw').send_keys(naver_pw)
pw_input = driver.find_element(By.ID, 'pw') 
pyperclip.copy(naver_pw) # control + c
pw_input.click()
pw_input.send_keys(Keys.COMMAND, 'v') # control + v
time.sleep(2)

# 로그인 버튼 클릭
driver.find_element(By.CLASS_NAME, "btn_login").click()
time.sleep(10)