import scrapper
from connect_database import connect_mongodb
from get_homepage import get_homepg_url
from get_topstories import top_story_url
from check_duplicate import article_exists
from store_data import store_mongodb
import logging

def main():
    url=get_homepg_url("url_config.json")
    top_story_link=top_story_url(url)
    news_data, article_urls, img_links = scrapper.scrape_google_news(top_story_link)
    collection_articles,collection_images=connect_mongodb()
    for (headline, image), article_url, img_link in zip(news_data, article_urls, img_links):
        if not article_exists(collection_articles,headline, article_url):
            store_mongodb(collection_articles,headline,article_urls,image,img_link,collection_images)
        else:
                logging.info(f"Skipping duplicate article: {headline}")
    # connect_mongodb(news_data, article_urls, img_links)
   
    

if __name__ == "__main__":
    main()