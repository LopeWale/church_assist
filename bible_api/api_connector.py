import requests
import time
from typing import Union

# Logging Setup
import logging
logging.basicConfig(filename='api_connector.log', level=logging.DEBUG)


class BibleAPI:
    BASE_URL = "https://bible-api.com/"
    RATE_LIMIT_DELAY = 60  # Delay for 60 seconds if rate-limited

    @classmethod
    def _make_request(cls, endpoint: str) -> Union[dict, None]:
        """Make a request to the Bible API and handle potential errors."""
        response = requests.get(cls.BASE_URL + endpoint)

        # Handle response based on status code
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            logging.error(f"Resource not found for endpoint: {endpoint}")
            return None
        elif response.status_code == 429:  # Rate Limit Exceeded
            logging.warning("Rate limit exceeded. Delaying for a while.")
            time.sleep(cls.RATE_LIMIT_DELAY)
            return cls._make_request(endpoint)
        else:
            logging.error(f"Unexpected error {response.status_code} for endpoint: {endpoint}")
            return None

    @classmethod
    def fetch_verse(cls, reference: str) -> Union[dict, None]:
        """Fetch verse data given a reference like 'John 3:16'."""
        return cls._make_request(reference)

    @classmethod
    def search_for_keyword(cls, keyword: str) -> Union[dict, None]:
        """Search for a keyword and fetch relevant verses."""
        endpoint = f"search/{keyword}"
        return cls._make_request(endpoint)


# Example Usage:
if __name__ == "__main__":
    bible = BibleAPI()
    result = bible.fetch_verse("John 3:16")
    if result:
        print(result['text'])  # Fetching the actual verse text from the result
