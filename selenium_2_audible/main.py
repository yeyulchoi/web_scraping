import pandas as pd
import until
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options   # run a bot
from time import sleep
options=Options()
options.headless = False
# options.add_argument('window-size=1920x1080')


website="https://www.audible.com/search"
path="C:\\chromedriver-win64\\chromedriver.exe"
service = Service(executable_path=path)
driver=webdriver.Chrome(service=service, options=options)
driver.get(website)
driver.maximize_window()  # headless is active , maximize_window doesn't work well

#pagination:
pagination = driver.find_element(By.XPATH,'//ul[contains(@class,"pagingElements")]')
pages=pagination.find_elements(By.TAG_NAME,'li')
last_page=int(pages[-2].text)
book_title = []
book_author = []
book_length = []


current_page=1
while current_page<=2:
    sleep(3)
    container= WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,'adbl-impression-container')))
    # container=driver.find_element(By.CLASS_NAME,'adbl-impression-container')
    products = WebDriverWait(container, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//li[contains(@class,"productListItem")]')))
    # products=container.find_elements(By.XPATH,'//li[contains(@class,"productListItem")]')



    for product in products:
        # print(product.text)
        book_title.append(product.find_element(By.XPATH,'.//h3[contains(@class,"bc-heading")]').text)
        book_author.append(product.find_element(By.XPATH, './/li[contains(@class,"authorLabel")]').text)
        book_length.append(product.find_element(By.XPATH, './/li[contains(@class,"runtimeLabel")]').text)

    current_page+=1
    try:
        next_page = driver.find_element(By.XPATH, '//span[contains(@class,"nextButton"]')
        next_page.click()
    except:
        pass



df=pd.DataFrame(
    {
        'book_title':book_title,
        'book_author':book_author,
        'book_length':book_length
    }
)
df.to_csv('try2.csv',index=False)
input('press enter')
driver.quit()