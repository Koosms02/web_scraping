import os 
import requests
from bs4 import BeautifulSoup
import uuid



folder_path = 'c:/Users/U20531232/Desktop/web_scraping/images'

search_params = os.listdir(folder_path)

print(search_params)


for name in search_params:
    print(type(name))
    print("---")