import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.shoprite.co.za/c-2413/All-Departments/Food'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
response = requests.get(url, headers=headers)

# fetching the web page
if response.status_code == 200:
    print('Successfully fetched the web page')
else:
    print('Failed to fetch the web page')

# Example: Extracting all the links from the webpage
soup = BeautifulSoup(response.content, 'html.parser')


links = soup.find_all('a')
foodItems =[]

for link in links:
    _links = link.get('href')

    if _links is not None:
        
        parts = _links.split('/')
        if len(parts) >= 4:
        #     # Extract the fourth element (index 3) after splitting
            category = parts[3]
            
            if category == "Food":
                foodItems.append(parts[len(parts)-1])
    
# food items are for image label
print(foodItems)

#loop for every food items and create a folder
folder_path = 'c:/Users/U20531232/Desktop/scraping _script/food/images/'

for i in range(0 , len(foodItems)):
    if not os.path.exists(folder_path +  foodItems[i]):
        # Create the folder
        os.mkdir(folder_path + foodItems[i])
        print(f"Folder '{folder_path}' created successfully.")
    else:
        print(f"Folder '{folder_path}' already exists.")


