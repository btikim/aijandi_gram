from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import pyautogui

driver = webdriver.Chrome('c:/imsi/chromedriver.exe')   # chrome 브라우저를 사용할 것이다
url = 'http://df.nexon.com/'
driver.get(url)
#time.sleep(0.3)
driver.maximize_window()      # 창을 최대로 키워라
action = ActionChains(driver)  # 창을 열어라

time.sleep(1)
driver.find_element_by_css_selector('.btn_log').click()    # id는 #으로 찾고, class는 점. 으로 찾는다.
time.sleep(1)
action.send_keys('psirimong@gmail.com').perform()   # 문자를 입력한다.
action.reset_actions()                  # action을 하고 나면 reset을 시켜주는 것이 좋다. 
time.sleep(1)
driver.find_element_by_css_selector('#txtPWD').send_keys('dunkim77!88')    # id는 #으로 찾고, class는 점. 으로 찾는다.
# pyautogui.typewrite("dunkim77!88")   # 문자를 입력한다.
time.sleep(1)
pyautogui.press('enter')     # 엔터키를 누른다

# driver.get('https://mail.google.com')   이와 같이 하면 해당 링크로 바로 이동한다
# driver.find_element_by_css_selector('.T-1.T-3').click()  class명이나 id에 공백이 포함되어 있으면 점. 으로 연결해줘야 한다.

# (                          # 괄호로 묶으면 괄호 안의 내용을 모두 한 줄로 인식한다.
# action.send_keys('btikim@gmail.com')
#         .key_down(Keys.TAB)   내용을 입력하고 TAB키를 누른다.
# )

# shift 키를 눌러서 대문자 입력하기
# .key_down(Keys.SHIFT).send_keys('abcdefg').key_up(Keys.SHIFT)

# .pause(2)   2초간 쉰다.

# 실제 마우스가 특정 위치로 이동한 후 클릭을 하게 만들려면 이렇게 코딩한다.

# send_button = driver.find_element_by_css_selector('.gU.Up')
# .move_to_element(send_button).click()