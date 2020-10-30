from selenium import webdriver
from selenium.webdriver.common.keys import Keys

ID = input("Enter your Id: ")
PWD = input("Enter your PWD: ")

PATH = "./chromedriver.exe"

# Setting up Webdriver
driver = webdriver.Chrome(PATH)
driver.get("https://gmail.com/")

# Scraping ID feild by xpath
id_input = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
id_input.send_keys(ID)
id_input.send_keys(Keys.RETURN)

'''
Waiting for the id feild to render data before switching to next page, to let net code wait for while
to prevent errors...
'''
driver.implicitly_wait(20)

# Scraping PWD feild by name attribute
pwd_input = driver.find_element_by_name('password')
pwd_input.send_keys(PWD)
pwd_input.send_keys(Keys.RETURN)

