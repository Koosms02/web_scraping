import os 
import requests
from bs4 import BeautifulSoup
import uuid



folder_path = 'G:\MACHINE_LEARNING\Training_Data\images'

search_params = os.listdir(folder_path)

print(search_params)


for name in search_params:
    print(name)
    print("---")