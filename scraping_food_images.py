import os 
import requests
from bs4 import BeautifulSoup





folder_path = 'c:/Users/U20531232/Desktop/scraping _script/'

file = os.listdir(folder_path)

if os.path.exists(folder_path + str("images")):
    print("paths exist")
else:  
    os.makedirs(folder_path + '/images' )

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
            foldername = product_name 

            # //create a folder with the product name 
            if os.path.exists(folder_path + "/images"+"/"+foldername ):
                print("The folder already exists")
            else:
                os.makedirs(folder_path + "/images"+"/"+foldername )

            product_image = 'https://www.shoprite.co.za/'+ item.find('div', class_='item-product__image __image').find('img')['data-original-src']
            
            # os.chdir(folder_path + "/images"+"/"+foldername )

            imgRes = requests.get(product_image, stream=True)
            filename = os.path.join(folder_path + "/images"+"/"+foldername , product_id+".png")

# Save the image to the specified directory
            with open(filename, 'wb') as image_file:
                for chunk in imgRes.iter_content(chunk_size=8192):
                  image_file.write(chunk)



            print("---")



for  i in range(0 , 175):
    url = 'https://www.shoprite.co.za/c-2413/All-Departments/Food?q=%3Arelevance%3AbrowseAllStoresFacetOff%3AbrowseAllStoresFacetOff&page='+ str(i)
    scrapeProducts(url)
      
