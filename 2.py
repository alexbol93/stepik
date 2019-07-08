import math
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")

# link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
# link.click()
#
# input1 = browser.find_element_by_tag_name("input.form-control[name=\"first_name\"]")
# input1.send_keys("Ivan")
# input2 = browser.find_element_by_name("last_name")
# input2.send_keys("Petrov")
# input3 = browser.find_element_by_class_name("form-control.city")
# input3.send_keys("Smolensk")
# input4 = browser.find_element_by_id("country")
# input4.send_keys("Russia")
# button = browser.find_element_by_css_selector("button.btn")
# button.click()
elements = browser.find_elements_by_css_selector("input[type = \"text\"]")
for element in elements:
    element.send_keys("Мой ответ")

button = browser.find_element_by_css_selector("button.btn")
button.click()
