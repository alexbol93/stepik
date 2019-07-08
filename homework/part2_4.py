import math
from selenium  import webdriver

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/execute_script.html")

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x = int(browser.find_element_by_id("input_value").text)
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

option1 = browser.find_element_by_id("robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
option1.click()

option2 = browser.find_element_by_id("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
option2.click()

button1 = browser.find_element_by_css_selector("button[type = \"submit\"]")
browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
button1.click()