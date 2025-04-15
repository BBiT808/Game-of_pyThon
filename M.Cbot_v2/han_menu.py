from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui
import pandas as pd
from bs4 import BeautifulSoup as bs
from datetime import datetime

def busan_menu(self):
    options = Options()
    options.binary_location = ".\\chrome-win64\\chrome.exe" # chrome 경로설정
    options.add_argument("--no-sanbox")# sandbox설정
    options.add_argument("--disable-dev-shm-usage") # 공유메모리 설정
    options.add_argument("--window-size=1920,1080") # 화면크기설정, 반응형 웹 대비
    
    service = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.pknu.ac.kr/main/399")
    
    hover_element = driver.find_element(By.CSS_SELECTOR, "#subCont > table > tbody > tr:nth-child(1) > td.bdlTitle > a")
    
    actions = ActionChains(driver)
    actions.move_to_element(hover_element).perform()
    
    time.sleep(1)
    hover_element.click()
    time.sleep(5)
    html = driver.page_source
    
    soup = bs(html,"html.parser")
    day = []
    day2 = []
    menu2 = []
    
    # 본문내용 가져오기
    for a in range(2,7):
        contents = soup.select(f"#subCont > div > div.bdvTxt_wrap > div > div > div:nth-child(18) > table > tbody > tr:nth-child(1) > td:nth-child({a})")
        for c in contents:
            a = c.get_text()
            day.append(a)
    # print(day)
    
    for a in range(1,6):
        contents = soup.select(f"#subCont > div > div.bdvTxt_wrap > div > div > div:nth-child(18) > table > tbody > tr:nth-child(2) > td:nth-child({a})")
        for c in contents:
            a = c.get_text()
            day2.append(a)
    # print(day2)
    
    for i in range(2,7):
        for a in range(1,11):
            contents = soup.select(f"#subCont > div > div.bdvTxt_wrap > div > div > div:nth-child(18) > table > tbody > tr:nth-child(3) > td:nth-child({i}) > p:nth-child({a}) ")
            for c in contents:
                a = c.get_text()
            menu2.append(a)
    # print(menu2)
    
    chunk_size = 10
    menu = [menu2[i:i+chunk_size] for i in range(0, len(menu2), chunk_size)]
    
    day = tuple(day)
    day2 = tuple(day2)
    menu = tuple(map(tuple, menu))
    
    print("이번주 한미락 메뉴입니다")
    for a in range(0,5):
        print(day2[a])
        print(day[a])
        print(menu[a])
        print("="*80)