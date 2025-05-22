from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv 

load_dotenv()

EMAIL=os.getenv("EMAIL")
PASSWORD=os.getenv("PASSWORD") 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
driver.maximize_window()

time.sleep(5)
button = driver.find_element(By.CSS_SELECTOR, ".sign-in-modal button")
button.click()

time.sleep(2)
print(EMAIL,PASSWORD)
email = driver.find_element(By.NAME, value="session_key")
email.send_keys(EMAIL)
password = driver.find_element(By.NAME, value="session_password")
password.send_keys(PASSWORD)
login_button = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
login_button.click()

time.sleep(5)
jobs = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container--clickable")
print(len(jobs))

for job in jobs:
    job.click()
    time.sleep(2)
    try:
        save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
        save_button.click()
        time.sleep(2)
        html = driver.find_element(By.TAG_NAME,value="html")
        html.send_keys(Keys.END)
        time.sleep(3)
        follow = driver.find_element(By.XPATH,value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/section/section/div[1]/div[1]/button')
        follow.click()
        time .sleep(2)
    except NoSuchElementException:
        continue
    



