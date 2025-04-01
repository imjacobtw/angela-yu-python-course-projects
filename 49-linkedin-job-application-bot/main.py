from dotenv import dotenv_values
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# With all due respect to the job posters, this project has been altered to save the job postings and follow the
# companies, rather than automating the job application process.

config = dotenv_values(".env")

LINKEDIN_JOB_POSTINGS_URL = config["LINKEDIN_JOB_POSTINGS_URL"]
LINKEDIN_EMAIL = config["LINKEDIN_EMAIL"]
LINKEDIN_PASSWORD = config["LINKEDIN_PASSWORD"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(LINKEDIN_JOB_POSTINGS_URL)

sign_in_button = driver.find_element(By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in_button.click()

email_input = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_key"]')
password_input = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_password"]')
email_input.send_keys(LINKEDIN_EMAIL)
password_input.send_keys(LINKEDIN_PASSWORD)

sign_in_button = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
sign_in_button.click()

# Timeout so the user can do any verification checks.
time.sleep(15)

job_postings_list = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/ul')
job_postings_list_container = job_postings_list.find_element(By.XPATH, "..")

# Scrolling multiple times to load all the jobs on the page.
for i in range(5):
    driver.execute_script("arguments[0].scrollBy(0, 1000)",job_postings_list_container)

job_posting_link_elements = job_postings_list.find_elements(By.CSS_SELECTOR, "a")
job_posting_links = [link_element.get_attribute("href") for link_element in job_posting_link_elements]

print(f"{len(job_posting_links)} jobs were found!")

for index, link in enumerate(job_posting_links):
    driver.get(link)
    job_title = driver.find_element(By.CSS_SELECTOR, ".job-details-jobs-unified-top-card__job-title h1").text
    job_company = driver.find_element(By.CSS_SELECTOR, ".job-details-jobs-unified-top-card__company-name a").text
    print(f"Job {index + 1}: {job_title} at {job_company}")

    save_button = driver.find_elements(By.CSS_SELECTOR, ".jobs-save-button")[1]

    if save_button.find_element(By.CSS_SELECTOR, ".jobs-save-button__text").text != "Saved":
        save_button.click()
        print("\tSaved!")
    else:
        print("\tAlready saved.")

    follow_button = driver.find_element(By.CSS_SELECTOR, ".follow")

    if follow_button.find_element(By.TAG_NAME, "span").text != "Following":
        follow_button.click()
        print("\tFollowed!")
    else:
        print("\tAlready followed.")
