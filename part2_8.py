from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

cost = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )
browser.find_element_by_id("book").click()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x = int(browser.find_element_by_id("input_value").text)

input1 = browser.find_element_by_id("answer")
input1.send_keys(calc(x))

button1 = browser.find_element_by_css_selector("button[type = \"submit\"]")
button1.click()