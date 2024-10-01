# +----------------------------------------------------------------------------+
# | CARDUI WORKS v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2024 - 2024, CARDUI.COM (www.cardui.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.cardui.com/carduiframework/license/license.txt
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: March 31st, 2024
# | Last update..: May 1st, 2024
# | WhatIs.......: Cookie Clicker Project - Main
# +----------------------------------------------------------------------------+
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from datetime import datetime

# Keep Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

store = driver.find_element(By.ID, value="store").text.split("\n")
print(store)

cursor = driver.find_element(By.ID, value="buyCursor").text.split("\n")
print(f"cursor: {cursor}")

store_items = {}
for i in range(0, len(store), 2):
    store_items.update(
        {
            store[i].split(" - ")[0]: store[i].split(" - ")[1]
        }
    )

print(f"store_items: {store_items}")

game_over = False

for i in range(0, 100):

    cookie.click()
    time.sleep(0.000000001)
    # print("Current Time =", datetime.utcnow())

money = int(driver.find_element(By.ID, value="money").text)
print(f"money: {money}")

test_store = driver.find_element(By.ID, value="store").text.split("\n")

time.sleep(10)

store = driver.find_element(By.ID, value="store").text.split("\n")
print(store)

# Close the window
driver.close()  # Close active tab
driver.quit()  # Quit the entire program
