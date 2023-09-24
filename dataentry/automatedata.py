import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def wait_for_success_message(driver, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if "Form submitted successfully" in driver.page_source:
            return True
        time.sleep(1)
    return False

def automate_data_entry(csv_filename):
    df = pd.read_csv(csv_filename)
    driver = webdriver.Chrome()  

    for index, row in df.iterrows():
        name = row['Name']
        age = row['Age']

    
        driver.get("file:///home/sriram/Documents/dataentry/form.html") 

        name_field = driver.find_element("name", "name") 
        name_field.send_keys(name)

        age_field = driver.find_element("name", "age")  
        age_field.send_keys(str(age))  
       
        submit_button = driver.find_element("xpath", "//input[@type='submit']")
        submit_button.click()

        if wait_for_success_message(driver):
            print("Form submitted successfully!")
        else:
            print("Timed out waiting for success message.")

        
        time.sleep(2)  =

    driver.quit()

if __name__ == "__main__":
    csv_filename = "data.csv"
    automate_data_entry(csv_filename)

