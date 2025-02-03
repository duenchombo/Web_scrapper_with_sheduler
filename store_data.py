import logging

def store_mongodb(articles_collection,Extracted_headline,Extracted_article_url,Extracted_img_link,Extracted_image_data,images_collection):
        # for (headline, image), article_url, img_link in zip(news_data, article_urls, img_links):
            # if not article_exists(headline, article_url):
                articles_collection.insert_one({
                    "headline": Extracted_headline,
                    "article_url": Extracted_article_url,
                    "img_link": Extracted_img_link
                })
                images_collection.insert_one({"image_data": Extracted_image_data})
                logging.info(f"Stored article: {Extracted_headline}")
            # else:
            #     logging.info(f"Skipping duplicate article: {Extracted_headline}")

# store_mongodb(news_data, article_urls, img_links)
logging.info("Script completed successfully")