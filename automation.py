from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PIL import Image
import pytesseract
import io

# Specify the path to ChromeDriver
chromedriver_path = r'C:\Users\Public\driver\chromedriver-win64\chromedriver.exe'

# Set up the ChromeDriver service
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

# Open irctc
driver.get('https://www.irctc.co.in/nget/train-search')
driver.maximize_window()

#add script
driver.implicitly_wait(3)
driver.find_element(By.XPATH, "//a[contains(text(),'LOGIN')]").click()
captcha_ss = driver.find_element(By.XPATH, "///img[@class='captcha-img']").screenshot_as_png

captcha_image = Image.open(io.BytesIO(captcha_ss))
captcha_text = pytesseract.image_to_string(captcha_image)
print("Extracted CAPTCHA text:", captcha_text)


driver.quit()
