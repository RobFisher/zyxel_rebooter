import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

debug = False
def dbg(s):
    if debug:
        print(s)

# Replace with your actual username and password
username = "admin"
password = os.environ["ROUTER_PASSWORD"]
address = os.environ["ROUTER_ADDRESS"]

# Configure Headless Firefox
options = webdriver.FirefoxOptions()
#options.headless = True
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

# Load the login page
dbg("Loading login page")
driver.get(f"http://{address}/login")

# test
#elements = driver.find_elements(By.XPATH, '//*[@id]')
#for x in elements:
#    print(x.tag_name, x.get_attribute('id'))

# Enter the username and password
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "userpassword").send_keys(password)

# Click the login button
dbg("Logging in")
driver.find_element(By.ID, "loginBtn").click()

# Wait for the login process to complete
wait = WebDriverWait(driver, 10)
wait.until(EC.url_changes(driver.current_url))

dbg("Logged in")

# test
#elements = driver.find_elements(By.XPATH, '//*[@id]')
#for x in elements:
#    print(x.tag_name, x.get_attribute('id'))

# reboot clicks
dbg('clicking menu')
driver.find_element(By.ID, "h_menu_list").click()
time.sleep(1)
dbg('clicking reboot')
driver.find_element(By.ID, "navbar_reboot").click()
time.sleep(1)

# test
#elements = driver.find_elements(By.XPATH, '//*[@id]')
#for x in elements:
#    try:
#       print(x.tag_name, x.get_attribute('id'))
#    except Exception:
#        pass

buttons = driver.find_elements(By.TAG_NAME, 'button')
dbg(len(buttons))

dbg('clicking ok')
buttons[-1].click()

# Close the browser
driver.quit()

