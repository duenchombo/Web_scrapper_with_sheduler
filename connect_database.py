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
