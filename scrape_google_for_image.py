import os 
import requests
from bs4 import BeautifulSoup
import uuid



folder_path = 'c:/Users/U20531232/Desktop/web_scraping/images'

search_params = os.listdir(folder_path)




# create a function to query 
def scrapeImages(query):

    url =   search_url = f'https://www.google.com/search?q={query}&sca_esv=578451392&rlz=1C1GCEA_enZA1082ZA1082&tbm=isch&sxsrf=AM9HkKmxewlWoDvPkelkhxcAtshxWB1Y1w:1698835600482&source=lnms&sa=X&ved=2ahUKEwiylP7jz6KCAxU1X0EAHZM7BXQQ_AUoAXoECAIQAw&cshid=1698835635819241&biw=1920&bih=912&dpr=1'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    

    folder_path = 'c:/Users/U20531232/Desktop/web_scraping/images'

    # paths to download to 

    # new_paths = folder_path + "/" + query

    items = soup.find_all('img')
    os.makedirs(os.path.join(folder_path, query), exist_ok=True)

    # items = soup.find_all('img')
    for idx, item in enumerate(items):
        img_url = item['src']
        if img_url.startswith('http'):
            try:
                # Generate a unique filename for each image
                img_name = str(uuid.uuid4()) + '.png'
                img_path = os.path.join(folder_path, query, img_name)

                # Download the image and save it as a PNG file
                with open(img_path, 'wb') as img_file:
                    img_data = requests.get(img_url).content
                    img_file.write(img_data)

                print(f"Image {idx + 1} downloaded: {img_path}")

            except Exception as e:
                print(f"Error downloading image {idx + 1}: {str(e)}")
    # print("scrape")


print("scraping start now -----")
for name in search_params:
    # if j == 0:
    scrapeImages(name)

print("scraping of images ends now ")

