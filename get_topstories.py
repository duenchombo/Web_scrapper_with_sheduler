import json
import logging
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



def top_story_url(homepage_url):
    options = Options()
    options.add_argument("--headless")  
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    driver = webdriver.Chrome(options=options)
    driver.get(homepage_url)
            
    top_news_element = driver.find_element(By.XPATH, '//*[@id="i11"]')
    top_news = top_news_element.get_attribute("href")
    driver.quit()
    
    return top_news