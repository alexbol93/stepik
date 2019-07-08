import os
from selenium  import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

name = browser.find_element_by_css_selector("input[name = \"firstname\"]").send_keys("Alex")
last_name = browser.find_element_by_css_selector("input[name = \"lastname\"]").send_keys("Bol")
email = browser.find_element_by_css_selector("input[name = \"email\"]").send_keys("123@123.wq")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, '1.txt')           # добавляем к этому пути имя файла

button_file = browser.find_element_by_id("file").send_keys(file_path)
button = browser.find_element_by_css_selector('button[type = "submit"]').click()