from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL= os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
SIMILIAR_ACCOUNT="chefsteps"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.instagram.com/chefsteps/")

time.sleep(5)
cookies = driver.find_element(By.XPATH,value='/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
cookies.click()

time.sleep(2)
login_button = driver.find_element(By.XPATH, value='/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[1]')
login_button.click()

time.sleep(2)
email = driver.find_element(By.NAME, value="username")
email.send_keys(EMAIL)
password = driver.find_element(By.NAME,value="password")
password.send_keys(PASSWORD)
button = driver.find_element(By.XPATH,value='/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[1]/div[3]/button')
button.click()

time.sleep(60)


