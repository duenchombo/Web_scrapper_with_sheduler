

def article_exists(articles_collection,headline, article_url):
        return articles_collection.find_one({"headline": headline, "article_url": article_url}) is not None