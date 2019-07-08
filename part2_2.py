import math
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

def calc(pic_atr):
    return str(math.log(abs(12 * math.sin(int(pic_atr)))))

pic = browser.find_element_by_id("treasure")
pic_atr = pic.get_attribute("valuex")

y = calc(pic_atr)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

option1 = browser.find_element_by_id("robotCheckbox")
option1.click()

option2 = browser.find_element_by_id("robotsRule")
option2.click()

button1 = browser.find_element_by_css_selector("button[type = \"submit\"]")
button1.click()

