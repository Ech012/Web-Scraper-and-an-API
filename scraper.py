#imports

#this is my web scraper built by echo

from bs4 import BeautifulSoup as bs 
import requests as rq
import random


#diffrent agente to be able to scrape the sote
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0"
]


#return the currency value in ils 
def get_price_ils(cur):

    HEADERS = {
    "User-Agent": f"{random.choice(USER_AGENTS)}"

        }

    try:
        URL = f"https://il.investing.com/currencies/{cur}-ils"
        raw_data = rq.get(URL, headers=HEADERS)
        html_content = bs(raw_data.text, "lxml")
        data = html_content.find("div", {"data-test": "instrument-price-last"})
        if data is None:
            return "Couldnt get the data"
        return data.text
        
    except Exception as e:
        return f"an error : {e}"
