from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

def testcase1():
	print("Test Case 1")
	driver.get("https://www.daraz.pk/")
	assert "Daraz.pk" in driver.title
	elem = driver.find_element(By.ID, "anonLogin")
	elem.click()
	assert "Welcome to Daraz! Please login" in driver.page_source
	print("Completed Test Case 1")

def testcase2():
	print("Test Case 2")
	driver.get("https://www.daraz.pk/")
	elem = driver.find_element(By.ID, "q")
	elem.send_keys("camera")
	elem.send_keys(Keys.RETURN)
	assert "No reuslt" not in driver.page_source
	print("Completed Test Case 2")

def testcase3():
	print("Test Case 3")
	driver.get("https://www.daraz.pk/")
	elem = driver.find_element(By.ID, "topActionCustomCare")
	elem.click()
	help = driver.find_element(By.CLASS_NAME, "care-item-anchor")
	help.click()
	assert "Help Center" in driver.title
	print("Completed Test Case 3")

testcase1()
testcase2()
testcase3()

driver.quit()
