import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/search?q=laptop+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=price_asc"

laptop_list = []
price_list = []
rating_list = []

for j in range(1, 10):  # scrape the first 3 pages
    r = requests.get(url+f"&page={j}")
    soup = BeautifulSoup(r.text, 'html.parser')
    box = soup.find("div",class_="_1YokD2 _3Mn1Gg")
    laptops = box.find_all("div",class_='_4rR01T')
    prices = box.find_all("div",class_="_30jeq3 _1_WHN1")
    ratings = box.find_all("div",class_="_3LWZlK")

    for laptop, price, rating in zip(laptops, prices, ratings):
        laptop_list.append(laptop.text)
        price_list.append(price.text)
        rating_list.append(rating.text.strip() if rating.text.strip() else None)

df=pd.DataFrame({"Laptop":laptop_list,"Price":price_list,"Ratings":rating_list})
print(df)
# df.to_csv("Flipkart_laptop.csv",index=False)
