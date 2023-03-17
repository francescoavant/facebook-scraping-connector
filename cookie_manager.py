from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from facebook_scraper import *
from random import randrange
import json


class cookie:
        def accounts(self,read_from_file = True):
                if read_from_file:
                        with open('accounts.json') as f:
                                accounts = json.load(f)
                count=0
                for account in accounts:
                        email=account["email"]
                        passw=account["pass"]
                        count+=1
                        self.create_cookie(email,passw,count)
                return count       

        def create_cookie(self,email,passw,count):
                
                chrome_options = webdriver.ChromeOptions()
                prefs = {"profile.default_content_setting_values.notifications" : 2}
                chrome_options.add_experimental_option("prefs",prefs)
                chrome_options.headless = True   
                chrome_options.add_argument("--log-level=3")              
                #driver.set_window_position(-10000,0)
                driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), chrome_options=chrome_options)
                driver.get("http://www.facebook.com")
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-cookiebanner="accept_button"]'))).click()

                username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
                password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
                username.clear()
                username.send_keys(email)
                password.clear()
                password.send_keys(passw)

                WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
                cookies_list=[]
                cookies_list.append(driver.get_cookie('c_user'))
                cookies_list.append(driver.get_cookie('xs'))
                filename= "./cookies/cookie"+str(count)+".json"
                #print(json.dumps(cookies_list,indent=4))
                with open(filename, "w") as f:
                        f.write(json.dumps(cookies_list, default=str, indent=4))
                return (json.dumps(cookies_list, default=str, indent=4))

        def rotatecookie(self, read_from_file= True):
                if read_from_file:
                        with open('accounts.json') as f:
                                accounts = json.load(f)
                count=0
                #len(account)
                for account in accounts:
                        count+=1
                num=randrange(count)
                print("using cookies num", num+1)
                return set_cookies('./cookies/cookie'+str(num+1)+'.json')              

#cookie().accounts()
