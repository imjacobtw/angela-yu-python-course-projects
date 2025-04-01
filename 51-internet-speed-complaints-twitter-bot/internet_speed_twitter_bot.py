from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self._driver = webdriver.Chrome(chrome_options)
        self._down: float = 0
        self._up: float = 0

    def get_internet_speed(self) -> None:
        self._driver.get("https://www.speedtest.net/")

        go_button_xpath = '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
        self._driver.find_element(By.XPATH, go_button_xpath).click()

        audience_survey_xpath = '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[4]/div/div/div[2]/div/div'
        WebDriverWait(self._driver, 180).until(ec.presence_of_element_located((By.XPATH, audience_survey_xpath)))

        test_results = self._driver.find_elements(By.CLASS_NAME, "result-data-large")
        self._down = float(test_results[0].text)
        self._up = float(test_results[1].text)

    def tweet_at_provider(self, email: str, password: str, promised_down: float, promised_up: float) -> None:
        self._driver.get("https://x.com/")

        sign_in_button_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div'
        WebDriverWait(self._driver, 5).until(ec.presence_of_element_located((By.XPATH, sign_in_button_xpath))).click()

        WebDriverWait(self._driver, 5).until(ec.presence_of_element_located((By.NAME, "text"))).send_keys(email)
        next_button_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]'
        self._driver.find_element(By.XPATH, next_button_xpath).click()
        WebDriverWait(self._driver, 5).until(ec.presence_of_element_located((By.NAME, "password"))).send_keys(password)

        login_button_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button'
        self._driver.find_element(By.XPATH, login_button_xpath).click()

        post_button_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a'
        WebDriverWait(self._driver, 5).until(ec.element_to_be_clickable((By.XPATH, post_button_xpath))).click()

        tweet_input_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div'
        tweet_input = WebDriverWait(self._driver, 5).until(ec.presence_of_element_located((By.XPATH, tweet_input_xpath)))
        tweet_input.click()
        message = f"Hey Internet Provider, why is my internet speed {self._down} down and {self._up} up, when I pay for {promised_down} down and {promised_up} up?"
        tweet_input.send_keys(message)

        post_button_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]'
        self._driver.find_element(By.XPATH, post_button_xpath).click()
