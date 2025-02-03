import json
import logging
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def setup_logging():
    """Configure logging to track script execution and errors."""
    logging.basicConfig(
        filename="news_scraper.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

def scrape_google_news(top_story_address):
    setup_logging()
    logging.info("Script started")
    
    options = Options()
    options.add_argument("--headless")  # Run in background
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    try:
        

        driver = webdriver.Chrome(options=options)
    
        driver.get(top_story_address)
        articles = driver.find_elements(By.XPATH, "//article[figure]")
        
        news_data, article_urls, img_links = [], [], []
        for article in articles:
            try:
                article_url = article.find_element(By.XPATH, "./div/a").get_attribute("href")
                img_tag = article.find_element(By.XPATH, ".//figure/img")
                img_link = img_tag.get_attribute("src")
                headline = article.find_element(By.CLASS_NAME, "gPFEn").text
                image = requests.get(img_link).content

                article_urls.append(article_url)
                img_links.append(img_link)
                news_data.append((headline, image))
            except Exception as e:
                logging.error(f"Error processing an article: {e}")
                continue
        driver.quit()
        return news_data, article_urls, img_links
    except Exception as e:
        logging.error(f"Script failed: {e}")