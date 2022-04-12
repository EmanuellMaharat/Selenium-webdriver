from selenium import webdriver

driver = webdriver.Firefox(executable_path=r"C:/webdeiver/geckodriver.exe")

driver.get("http://www.youtube.com")