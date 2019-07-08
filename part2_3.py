from selenium  import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects2.html")

value_1 = browser.find_element_by_id("num1")
x = value_1.text
value_2 = browser.find_element_by_id("num2")
y = value_2.text

sum = str(int(x) + int(y))

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(sum)

button1 = browser.find_element_by_css_selector("button[type = \"submit\"]")
button1.click()
