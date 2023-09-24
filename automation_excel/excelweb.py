from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import openpyxl

# Set up the web driver (make sure you have the appropriate driver installed)
driver = webdriver.Chrome()

# Open the local HTML file
driver.get("file:///path/to/your/form.html")  # Replace with the actual file path

# Find the input field and submit button and interact with them
input_field = driver.find_element_by_id("inputField")
input_value = "Your Value"
input_field.send_keys(input_value)

submit_button = driver.find_element_by_id("submitButton")
submit_button.click()

# Wait for a bit to let the page load (adjust the time as needed)
time.sleep(2)

# Initialize Excel workbook and sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# Write the value to the Excel sheet
sheet["A1"] = input_value

# Save the Excel file
workbook.save("data.xlsx")

# Close the browser
driver.quit()

