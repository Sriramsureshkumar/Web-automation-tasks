from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")

search_input = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")

search_input.send_keys("laptop")
search_input.send_keys(Keys.RETURN)  

driver.quit()

