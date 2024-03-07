import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import asyncio
import random
import datetime

def login():
    # Click login button
    elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div[1]/div/div[3]/div/a[2]")
    elem.click()
    
    time.sleep(2)
    # Enter Username
    elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input")
    elem.send_keys(os.getenv('STEAMUSER'))
    
    # Enter Password
    elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/form/div[2]/input")
    elem.send_keys(os.getenv('STEAMPASS'))
    
    # Click the sign in button
    elem  = driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/form/div[4]/button")
    elem.click()
    
def getCode(): # Allows the user to submit the steam guard code
    print("Get the code from the email")
    code = input()
    itr = 1
    for i in code:
        elem = driver.find_element(By.XPATH,f"/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/form/div/div[2]/div[1]/div/input[{itr}]")
        elem.send_keys(i)
        itr = itr+1
    
async def comment():
    #Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    #Find the comment field and type "bump"
    elem = driver.find_element(By.ID, "commentthread_ForumTopic_103582791432321297_864961175647450868_3069740688716495769_textarea")
    elem.send_keys("bump")
    
    elem = driver.find_element(By.ID, "commentthread_ForumTopic_103582791432321297_864961175647450868_3069740688716495769_submit")
    elem.click()
    
async def periodic():
    print("Beginning bumping...")
    while True:
        now = datetime.datetime.now()
        if (now.hour < 22 and now.hour > 7):
            await comment()
        await asyncio.sleep(random.randint(3400, 3800))
         
if __name__ == '__main__':
    load_dotenv()
    driver = webdriver.Firefox()
    driver.get(os.getenv('STEAMLINK'))
    login()
    getCode()
    time.sleep(15)
     
    loop = asyncio.get_event_loop()
    task = loop.create_task(periodic())
    
    loop.run_until_complete(task)
