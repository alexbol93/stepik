from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/redirect_accept.html")
browser.find_element_by_tag_name("button").click()

browser.switch_to.window(browser.window_handles[1])

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x = int(browser.find_element_by_id("input_value").text)

input1 = browser.find_element_by_id("answer")
input1.send_keys(calc(x))

button1 = browser.find_element_by_css_selector("button[type = \"submit\"]")
button1.click()