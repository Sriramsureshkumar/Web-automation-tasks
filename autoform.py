from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSek4lvyKCkjeKHJwRRSUdsNb4WCIohFNlog7YjeWVzmEr3DQQ/viewform')

time.sleep(2)

LastName = "Sriram"
last = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
last.send_keys(LastName)

FirstName = "Suresh"
first = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
first.send_keys(FirstName)

RadioButtonPeriod = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
RadioButtonPeriod.click()

Submit = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
Submit.click()

try:
    confirmation_message_locator = (By.CSS_SELECTOR, '.freebirdFormviewerViewResponseConfirmationMessage')
    confirmation_message = WebDriverWait(web, 100).until(EC.visibility_of_element_located(confirmation_message_locator))
    print(confirmation_message.text)

    if confirmation_message.text == "Thank you for attending":
        print("Test Was Successful")
    else:
        print("Test Was Not Successful")
except Exception as e:
    print("Error:", str(e))

web.quit()

