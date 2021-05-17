import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# MAKE SURE YOU CLOSE ALL TABS BEFORE RUNNING THE SCRIPT
# CHANGE YOUR USERNAME IN ENVIRONMENT VAR TO YOUR MACHINE'S USER
# MAKE SURE YOU ARE LOGGED INTO WATERLOOWORKS BEFORE RUNNING THE SCRIPT

# environment variables
username = "USERNAME"
timeout = 5

# set up chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--user-data-dir=C:/Users/" + username + "/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(options=chrome_options)

# start doing da work
driver.maximize_window()
url = "https://waterlooworks.uwaterloo.ca/myAccount/co-op/coop-postings.htm"
driver.get(url)

try:
	element_present = EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Shortlist'))
	WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
	print("Timed out waiting for page to load")

time.sleep(2)

# click into shortlist
driver.execute_script("arguments[0].click()", driver.find_element_by_partial_link_text('Shortlist'))

try:
	element_present = EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Apply'))
	WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
	print("Timed out waiting for page to load")

apply_links = driver.find_elements_by_partial_link_text('View')

for link in apply_links:
	# open app window and load
	driver.execute_script("arguments[0].click()", link)
	driver.execute_script("arguments[0].click()", driver.find_element_by_partial_link_text('new tab'))
	
	window_before = driver.window_handles[0]
	window_after = driver.window_handles[1]

	driver.switch_to.window(window_after)

	try:
		element_present = EC.presence_of_element_located((By.ID, 'volume-booster-visusalizer'))
	except TimeoutException:
		print("Timed out waiting for page to load")

	# if the apply button exists, click it
	try:
		apply_btn = driver.find_element_by_partial_link_text('APPLY')
		driver.execute_script("arguments[0].click()", apply_btn)
	except:
		print('Already Applied')
		driver.close()
		driver.switch_to.window(window_before)
		continue
	
	#check if apply with an existing app package exists; submit with default if exists
	try:
		default_package = driver.find_element_by_xpath("//input[@value='defaultPkg']")
		driver.execute_script("arguments[0].click()", default_package)
		submit_app = driver.find_element_by_xpath("//input[@value='Submit Application']")
		driver.execute_script("arguments[0].click()", submit_app)
	except:
		print('Not A Default Package')
		driver.close()
		driver.switch_to.window(window_before)
		continue

	# go back
	driver.close();
	driver.switch_to.window(window_before)

print('Finished Applying')