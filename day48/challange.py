from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome()
driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME,value="email")
fname.send_keys("Michal")
lname.send_keys("Jazdowski")
email.send_keys("majkivalorantsamsung@gmail.com")
button = driver.find_element(By.CSS_SELECTOR, value="form button")
button.click()