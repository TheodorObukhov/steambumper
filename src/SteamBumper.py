#recruiting 'bump' script
#This one requires you to keep it up 24/7. If not you will have to reinput your steam access code EVERY SINGLE TIME.

#A lot of the script is copied and pasted from the RedditPoster so if you'd like the see some more detailed comments just go there and it'll probably apply here.
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
import time
import random
from random import randint
from operator import add, sub
import datetime
#global
userN = ("[Input Username]")
passW = ("[Input Password]")
web = ("https://steamcommunity.com/app/107410/discussions/10/3069740688716495769/")

def get_time() -> str: #Dont fucking touch it, it will take the time from your computer so it automatically adjusts for time zones.
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def bump_loop(): #This actually makes the reply to the dicussion. You can change what it says with the "comment" variable.
    comment = ("bump")
    comment_field = driver.find_element(By.XPATH, '//*[@id="commentthread_ForumTopic_103582791432321297_864961175647450868_3069740688716495769_textarea"]')
    ActionChains(driver).move_to_element(comment_field).click(comment_field).send_keys(comment).perform()
    while True:
        try:
            driver.find_element(By.XPATH, '//*[@id="commentthread_ForumTopic_103582791432321297_864961175647450868_3069740688716495769_submit"]')
            break
        except NoSuchElementException:
            print("Could not find comment button. Trying again.")
            time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="commentthread_ForumTopic_103582791432321297_864961175647450868_3069740688716495769_submit"]').click()
    ActionChains(driver).reset_actions()
    print("Success! Time waiting:", ansRnd,"hrs.", " Timestamp:", get_time())

if __name__ == "__main__":
    #page
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(web) #This is the link to my post for our unit but you can make a new one and just replace the link.
    driver.set_window_size(1000,800)
    #login
    userN = ("[Input Username]")
    passW = ("[Input Password]")
    while True:
        try:
            driver.find_element(By.XPATH, '//*[@id="global_action_menu"]/a').click()
            break
        except:
            print("Cannot find login button. Trying again.")
            time.sleep(1)
    loginButton = driver.find_element(By.XPATH, '//*[@id="global_action_menu"]/a')
    loginButton.click()
    while True:
        try:
            driver.find_element(By.XPATH, '//*[@id="input_username"]')
            break
        except NoSuchElementException:
            print("Cannot find username field. Trying again.")
            time.sleep(1)
    username = driver.find_element(By.XPATH, '//*[@id="input_username"]')
    ActionChains(driver).move_to_element(username).click(username).send_keys(userN).perform()
    password = driver.find_element(By.XPATH ,'//*[@id="input_password"]')
    ActionChains(driver).reset_actions()
    ActionChains(driver).move_to_element(password).click(password).send_keys(passW).perform()
    signin = driver.find_element(By.XPATH ,'//*[@id="login_btn_signin"]/button').click()
    while True:
        try:
            driver.find_element(By.XPATH, '//*[@id="commentthread_ForumTopic_103582791432321297_864961175647450868_3069740688716495769_textarea"]')
            break
        except NoSuchElementException:
            print("Cannot find comment field field. Trying again.")
            time.sleep(1)

    #Dont touch this
    while True:
        now = datetime.datetime.now()
        nowHour = '{:02d}'.format(now.hour)
        nowHourInt = int(nowHour)
        rand_int = randint(120, 600)
        ops = (add, sub)
        op = random.choice(ops)
        beg = random.randint(120, 600)
        ans = op(3600, beg)
        ansRndSet = (ans/3600)
        ansRnd = str(round(ansRndSet,2))

        #If the time is before 21:00 and after 06:00, it will bump. If it is in between those hours, it will sleep. You can change these for yourself.
        if nowHourInt < 22 and nowHourInt > 7:
            bump_loop()
            time.sleep(ans)
        else:
            print("Sleeping. Current time:", get_time())
            time.sleep(ans)