import json
import logging
# "url_config.json"

def get_homepg_url(json_config_url):
    try:
        with open(json_config_url, "r") as config_file:
            config = json.load(config_file)
            url = config.get('url')
        return url
    except Exception as e:
        logging.error(f"failed to get homepage: {e}")
     