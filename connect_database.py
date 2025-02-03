import logging
from pymongo import MongoClient


def connect_mongodb():
    try:
        client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=5000")
        db = client.BREAKING_NEWS
        articles_collection = db.ARTICLES
        images_collection = db.IMAGES
        logging.info("Connected to MongoDB successfully!")
        print("Connected to MongoDB successfully!")
        return articles_collection,images_collection
            
    except Exception as e:
        logging.error(f"Error connecting to MongoDB: {e}")
        return

    # def article_exists(head, article):
    #     return articles_collection.find_one({"headline": head, "article_url": article}) is not None

    # def store_news_data(news_data, article_urls, img_links):
    #     # for (headline, image), article_url, img_link in zip(news_data, article_urls, img_links):
    #         # if not article_exists(headline, article_url):
    #             articles_collection.insert_one({
    #                 "headline": headline,
    #                 "article_url": article_url,
    #                 "img_link": img_link
    #             })
    #             images_collection.insert_one({"image_data": image})
    #             logging.info(f"Stored article: {headline}")
    #         else:
    #             logging.info(f"Skipping duplicate article: {headline}")

    # store_news_data(news_data, article_urls, img_links)
    # logging.info("Script completed successfully")
