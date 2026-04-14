from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import undetected_chromedriver as uc

options = Options()
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--profile-directory=Default")
options.add_argument("--password-store=basic")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1345x610")



driver = webdriver.Chrome(options=options)
driver.set_window_size(1354, 610)
actions = ActionChains(driver)


