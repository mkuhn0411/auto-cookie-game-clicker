from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("/Users/melaniekuhn/Desktop/Udemy_Python")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

timeout = time.time() + 5
five_min = time.time() + 60 * 5

site = driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
store = driver.find_element(By.ID, "store")


def get_available_items():
    available_items = {int(item.text.split("-")[1].split("\n")[0].strip()): item.text.split("-")[0].strip() for item in store.find_elements(By.CSS_SELECTOR, "div:not(.grayed):not(.amount)")}
    return available_items


def get_best_item():
    items = get_available_items()
    costs = [key for key,value in items.items()]
    max_value = max(costs)
    best_item_element = driver.find_element(By.ID, f"buy{items[max_value]}")
    return best_item_element


while True:
    cookie.click()

    # checks every 5 seconds
    if time.time() > timeout:
        best_item = get_best_item()
        best_item.click()
        timeout = time.time() + 5

    if time.time() > five_min:
        cookies_amount = driver.find_element(By.ID, "money")
        print(cookies_amount.text)

