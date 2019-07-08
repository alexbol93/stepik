import math
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

option1 = browser.find_element_by_id("robotCheckbox")
option1.click()

option2 = browser.find_element_by_id("robotsRule")
option2.click()

button1 = browser.find_element_by_css_selector("button[type = \"submit\"]")
button1.click()



