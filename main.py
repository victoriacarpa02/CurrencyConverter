from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Currency:
    def __init__(self, curFrom, curTo):
        self.currencies = [curFrom, curTo]

        # set currencies
        self.set_currency()

    def set_currency(self):
        # wait for page loading
        time.sleep(3)

        # select currency that you have
        select_currencies = browser.find_elements(By.CLASS_NAME, 'sc-184232u-1')
        for i, option in enumerate(select_currencies):
            option.click()
            # scroll the container to the end so that all elements are available for selection
            scroll_element = browser.find_element(By.CLASS_NAME, 'sc-184232u-2')
            for _ in range(10):
                browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scroll_element)
                time.sleep(0.1)
            # find and click on a specific currency
            browser.find_element(By.XPATH, f'//button[@data-value="{self.currencies[i]}"]').click()

    def exchange(self, value):
        # enter value
        fields = browser.find_elements(By.CLASS_NAME, 'zlkj5-1')
        fields[0].clear()
        fields[0].send_keys(value)

        # return result
        return f"{value} {self.currencies[0]} --> {fields[1].get_attribute('value')} {self.currencies[1]}"


with webdriver.Firefox() as browser:
    browser.get('https://minfin.com.ua/currency/converter/')

    obj = Currency('USD', 'EUR')
    print(obj.exchange(450))
    print(obj.exchange(32))
    print(obj.exchange(90.56))

    obj = Currency('PLN', 'UAH')
    print(obj.exchange(450))
    print(obj.exchange(32))
    print(obj.exchange(90.56))
