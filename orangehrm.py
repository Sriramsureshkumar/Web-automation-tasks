from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

wait = WebDriverWait(driver, 10)  
time.sleep(1)
username = wait.until(EC.presence_of_element_located((By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]")))
username.send_keys('admin')

time.sleep(2)
password= wait.until(EC.presence_of_element_located((By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[2]/input[1]")))
password.send_keys('admin123')

time.sleep(1)

login= wait.until(EC.presence_of_element_located((By.XPATH,"//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]")))
login.click()
time.sleep(1)


Pim=wait.until(EC.presence_of_element_located((By.XPATH,"//body/div[@id='app']/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[2]/a[1]")))
Pim.click()

time.sleep(1)
pimadd= wait.until(EC.presence_of_element_located((By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/button[1]")))
pimadd.click()
time.sleep(1)
firstname= wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='firstName']")))
firstname.send_keys('Sriram')
time.sleep(1)
lastname= wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='lastName']")))
lastname.send_keys('Suresh')
time.sleep(1)
pimadd= wait.until(EC.presence_of_element_located((By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/button[2]")))
pimadd.click()
time.sleep(1)
time.sleep(10)
driver.quit()
