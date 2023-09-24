from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome()

# Open the Google homepage
driver.get("https://www.google.com")

# Find the search bar element and input the search query
search_box = driver.find_element("name", "q")
search_query = "What is devops"
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)  # Press Enter

# Wait for the search results to load
time.sleep(5)

# Print the title of the search results page
print(driver.title)

# Close the browser
driver.quit()

