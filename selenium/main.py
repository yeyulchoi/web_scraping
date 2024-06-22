import time

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

website="https://www.adamchoi.co.uk/overs/detailed"
path ="C:\\chromedriver-win64\\chromedriver.exe"
service = Service(executable_path=path)
driver=webdriver.Chrome(service=service)
driver.get(website)

all_matches_button=driver.find_element(By.XPATH,'//label[@analytics-event="All matches"]')
all_matches_button.click()

dropdown=Select(driver.find_element(By.ID,'country'))
dropdown.select_by_visible_text('South Korea')

time.sleep(3)


date=[]
home_team=[]
score=[]
away_team=[]

matches=driver.find_elements(By.TAG_NAME,'tr')
for a in matches:
    print(a.text[0])

for match in matches:
    date.append(match.find_element(By.XPATH,'./td[1]').text)
    home=match.find_element(By.XPATH, './td[2]').text
    home_team.append(home)
    print(home)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    away_team.append(match.find_element(By.XPATH, './td[4]').text)
input("Prscript...")


input("Press Enter to close the browser and end the script...")
df = pd.DataFrame(
    {'date': date,
     'home_team':home_team,
     'score':score,
     'away_team':away_team}
)
df.to_csv('new_file.csv',index=False)

input('press enter')

driver.quit()