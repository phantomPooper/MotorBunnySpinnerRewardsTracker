from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import time
import clipboard


def random_char(char_num: int, string_type: str):
    return ''.join(random.choice(string_type) for _ in range(char_num))


# CHANGE THESE PARAMS
# How many instances you wish to record
LOOP_COUNT = 1000
# Fully Qualified File path and file name you wish to record to
FULLY_QUALIFIED_FILE_PATH = 'c:\\users\\chad\\desktop\\motorbunny_codes.txt'

i = 0
driver = webdriver.Firefox()
driver.get('https://motorbunny.com/')

while True:

    try:
        if i == LOOP_COUNT :
            break

        # enter email
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'wlo-trigger-image'))).click()
        element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "wlo-email-input")))
        element.click()
        element.send_keys(f'{random_char(random.randint(6, 10), string.ascii_letters)}@{random_char(random.randint(4, 6), string.ascii_letters)}.com')

        # enter phone number
        element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'wlo-phoneNumber-input')))
        element.click()

        # Change to valid phone number
        # using hardcoded Maryland Domino's Pizza number bc random strings weren't reliably valid
        # element.send_keys(random_char(10, string.digits))
        element.send_keys('3016995880')

        # check terms and conditions and click spin
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'wlo-sms-checkboxInput'))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'wlo-btn-wlo-pulse'))).click()

        # wait for spin
        time.sleep(8)

        # get discount amount
        discount_amount = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="wlo-font-color"]//span'))).text

        # get discount code - can't be gotten via html text, only by clipboard
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'wlo-copy-button'))).click()
        code = clipboard.paste()

        # write code to file
        with open(FULLY_QUALIFIED_FILE_PATH, 'a') as f:
            f.write(f'{discount_amount}: {code}\n')

        print(f'{i}) {discount_amount}: {code}')

        # increment i to end loop condition
        i += 1

    except TimeoutError:
        print('timeout')

    # bare except bad
    except:
        print('failed')

    finally:
        driver.execute_script("location.reload(true);")

# quit driver & close file
driver.quit()
