import os 
import requests
from bs4 import BeautifulSoup





folder_path = 'c:/Users/U20531232/Desktop/scraping _script/food/images/'

file = os.listdir(folder_path)


# items = soup.find_all('div' , class_ ="product__listing product__grid")

#looping through the items

# print(items)


def scrapeProducts(url ):
   

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    
    items = soup.find_all('div', class_='product-frame')
    for item in items:
            parts =  item.find('h3', class_='item-product__name').text.strip().split()  # Split the string into words

            # Join all parts except the last one


            product_id = item['data-product-ga'].split('"id": "')[1].split('"')[0]
            product_name = ' '.join(parts[:-1])
            product_price = item.find('div', class_='special-price__price').text.strip()
            product_image = 'https://www.shoprite.co.za/'+ item.find('div', class_='item-product__image __image').find('img')['data-original-src']
            
            
            print(f"Product ID: {product_id}")
            print(f"Product Name: {product_name}")
            print(f"Product Price: {product_price}")
            print(f"Product Price: {product_image}")
            print("---")



for  i in range(0 , 1):
    url = 'https://www.shoprite.co.za/c-2413/All-Departments/Food?q=%3Arelevance%3AbrowseAllStoresFacetOff%3AbrowseAllStoresFacetOff&page='+ str(i)
    scrapeProducts(url)
      
