import os 
import requests
from bs4 import BeautifulSoup
import uuid

file_path = "labels.txt"

folder_path = 'G:\MACHINE_LEARNING\Training_Data\images'

search_params = os.listdir(folder_path)


print("now writing to a file")
with open(file_path, 'w') as file:
    for name  in search_params:
        file.write(name +'\n')


print("done writing to a file")