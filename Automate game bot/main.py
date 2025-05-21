from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
elements = driver.find_elements(By.CLASS_NAME, value="grayed")
elements.pop()
items = [element.get_attribute("id") for element in elements]
timeout = time.time() + 5
stopper = time.time() + 60*5
print(items)
game_on = True

while game_on:
    cookie.click()
    if time.time() > timeout:
        buy_index = 0
        prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        prices.pop()
        price_list = [int(price.text.replace(" ","").split("-")[1].replace(",","")) for price in prices]
        for price in price_list:
            money = int(driver.find_element(By.ID, value="money").text.replace(",",""))
            if money > price:
                buy_index = price_list.index(price)
        print(buy_index)
        item_buy = driver.find_element(By.ID, value=items[buy_index])
        print(item_buy)
        item_buy.click()
        timeout = time.time() + 5
    if time.time() > stopper:
        cookies = driver.find_element(By.ID,value="cps").text
        print(f"cookies/second: {cookies}")
        game_on = False

    
        


