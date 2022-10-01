
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Software Testing\Automation\webdriver\chromedriver.exe")     # Creating class object of Chrome
driver.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

time.sleep(3)
# Page scroll by pixel
driver.execute_script('window.scrollBy(0, 3000)', "")


time.sleep(3)
# Scroll by or upto specific element
ele = driver.find_element(By.ID, 'Programming_examples')
driver.execute_script("arguments[0].scrollIntoView()", ele)


time.sleep(3)
## scroll till the end of page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)", "")


time.sleep(3)
## scroll upside
driver.execute_script("window.scrollBy(0, -3000)", "")

time.sleep(3)
## scroll to top of the page
driver.execute_script("window.scrollTo(0,0)", "")

# diff bet scrollBy and scrollTo



