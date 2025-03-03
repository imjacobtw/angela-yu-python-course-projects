from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()

cookie_element = driver.find_element(By.ID, "cookie")

upgrade_timeout_start = time.time()
quit_timeout_start = time.time()
upgrade_timeout_duration = 5
quit_timeout_duration = 60 * 5

while time.time() < quit_timeout_start + quit_timeout_duration:
    cookie_element.click()

    if time.time() >= upgrade_timeout_start + upgrade_timeout_duration:
        upgrade_timeout_start = time.time()
        store_elements = driver.find_elements(By.CSS_SELECTOR, '#store div[class=""]')
        if store_elements:
            store_elements[-1].click()

cookies_per_second_element = driver.find_element(By.ID, "cps")
print(cookies_per_second_element.text)
driver.close()