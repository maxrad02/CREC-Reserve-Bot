from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Change these values to your NUID and Password
username = "NUID"
password = "PASSWORD"

# Change this value to the time you would like to resever
# MUST BE in correct format! i.e. "3:00" or "10:30"
reserveTime = "3:00"

# This value will be True if you want to reserve for the current day
# This value will be False if you want to reserve for next day (default)
reserveForToday = False

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

# Change this path to where you downloaded the chromedriver
browser = webdriver.Chrome(executable_path=r"C:/PATH TO WEBDRIVER", options=options)
browser.maximize_window()
browser.get("https://shopcrec.unl.edu/webportal.html")

### Start ###

# Click login button
WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.ID, "ms_col_one"))
).click()

### New Page ###

# Fill in username
usernameText = WebDriverWait(browser, 20).until(
    EC.visibility_of_element_located((By.ID, "username"))
)
usernameText.send_keys(username)

# Fill in password
passwordText = WebDriverWait(browser, 20).until(
    EC.visibility_of_element_located((By.ID, "password"))
)
passwordText.send_keys(password)

# Hit submit
WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
).click()

### New page ###

# Wait to switch to duo frame
WebDriverWait(browser, 20).until(
    EC.visibility_of_element_located((By.XPATH, "//iframe"))
)
browser.switch_to.frame(0)

# Click send push button
WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button"))
).click()

# Switch back to default frame
browser.switch_to.default_content()

### New page ###

# Click stength and training
WebDriverWait(browser, 80).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[text()='Strength Training Reservations']")
    )
).click()

### New page ###

# Click strength and training CREC
WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'result-content')]"))
)
crec = browser.find_elements_by_xpath("//*[contains(@class, 'result-content')]")[1]
crec.click()

# Click on reservation time
WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[text()='CREC - " + reserveTime + " pm Extended Reservation']")
    )
).click()

### New page ###

# Click Add to cart
WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text()='Add To Cart']"))
).click()

### New page ###

# Gets all days
WebDriverWait(browser, 20).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(@class, 'calendar__day')]")
    )
)
days = browser.find_elements_by_xpath("//*[contains(@class, 'calendar__day')]")

# Finds the next day
for i in range(len(days)):
    if days[i].get_attribute("class") == "calendar__day calendar__day--state-today":
        reserveDay = days[i + 1] if reserveForToday else days[i + 6]

# Clicks the next day
reserveDay.find_element_by_xpath(".//*[contains(@class, 'calendar__block')]").click()

# Click add to cart again
WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(@class, 'multiselectlist__addbutton')]")
    )
).click()

### New page ###

# Click checkout
WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.ID, "webcart_buttoncheckout"))
).click()

### New page ###

# Click continue
WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.ID, "webcheckout_buttoncontinue"))
).click()
