from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# Specify the path to ChromeDriver
chromedriver_path = r'C:\Users\Public\driver\chromedriver-win64\chromedriver.exe'

# Set up the ChromeDriver service
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

# Open irctc
driver.get('https://www.irctc.co.in/nget/train-search')
driver.maximize_window()

#add script


driver.quit()

