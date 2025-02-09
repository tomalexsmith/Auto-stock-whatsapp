# Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# Misc imports
from time import sleep
import os

class whatsapp_client():

    def __init__(self, headless=True):
        self.message = ["Test"]
        self.headless = headless

    def send_message(self, message=None):
        
        # Set message to test if no parameter is defined
        messages = message.split("\n") if message is not None else self.message 
        multiline = True if len(messages) > 1 else False
  
        # Trim whitespace on messages
        for x, message in enumerate(messages):
            
            message = message.strip()
            
            # Replace specified blank line character
            if message == "~":
                messages[x] = " "
            else:
                messages[x] = message
        
        
        # Make Chrome browser headless
        chrome_options = Options()
        
        if self.headless:
            chrome_options.add_argument("--headless=new")

        dir_path = os.getcwd()
        profile = os.path.join(dir_path, "profile", "wpp")

        chrome_options.add_argument(r"user-data-dir={}".format(profile))
        driver = webdriver.Chrome(options=chrome_options)

        driver.get("https://web.whatsapp.com/")
        sleep(5)
        driver.find_element(
            By.XPATH,
            '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div/span[1]',
        ).click()
        
        # Send messages
        
        message_input_box = driver.find_element(
                By.XPATH,
                '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]',
            )
        
        for message in messages:
            
            message_input_box.send_keys(message if len(message) > 0 else " ")
            
            if len(message) < 1:
                print("Test")
            
            if multiline and message != messages[-1]:
                
                actions = ActionChains(driver)
                actions.key_down(Keys.LEFT_SHIFT).send_keys(Keys.RETURN).key_up(Keys.LEFT_SHIFT).perform()
            
            else:
                message_input_box.send_keys(Keys.RETURN)        

        sleep(3)
        driver.close()