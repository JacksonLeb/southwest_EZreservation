import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from cred import first_name, last_name

# initalizing chromedriver
driver = webdriver.Chrome('/Users/jacksonleb/downloads/chromedriver')
url = "https://mobile.southwest.com/check-in"
driver.get(url)
time.sleep(1)

# inputting confirmation num, first and last name
confirmation_num = input("Confirmation Number: ")
confirmation_num_input = element = driver.find_element(
    By.CSS_SELECTOR, "#appContents > div.check-in > div > div.reservation-retrieval-form > div > form > fieldset > div > div:nth-child(1) > div > input")
confirmation_num_input.send_keys(confirmation_num)

first_name_input = driver.find_element(
    By.CSS_SELECTOR, "#appContents > div.check-in > div > div.reservation-retrieval-form > div > form > fieldset > div > div:nth-child(2) > div > input")
first_name_input.send_keys(first_name)

last_name_input = driver.find_element(
    By.CSS_SELECTOR, "#appContents > div.check-in > div > div.reservation-retrieval-form > div > form > fieldset > div > div:nth-child(3) > div > input")
last_name_input.send_keys(last_name)

while(True):
    try:
        retrieve_reservation = driver.find_element(
            By.CSS_SELECTOR, "#appContents > div.check-in > div > div.reservation-retrieval-form > div > form > fieldset > div > div.segment > button")
        retrieve_reservation.click()
    except NoSuchElementException as exception:
        print("Couldn't Find Element")

    warning_ok = WebDriverWait(driver, 5).until(lambda d: d.find_element(
        By.CSS_SELECTOR, "#app > div:nth-child(1) > div > div.popup-container.popup-showing.active > div > div.popup-buttons > div > div > button"))
    warning_ok.click()
