import requests
from bs4 import BeautifulSoup
import pandas as pd
books=[]
for i in range(1,5):
  url=f"https://books.toscrape.com/catalogue/page-{i}.html"
  response=requests.get(url)
  response=response.text
  soup=BeautifulSoup(response,'html.parser')
    # print(soup)
  ol=soup.find('ol')
  articles=ol.find_all('article',class_="product_pod")

  for i in articles:
    image=i.find("img")
    title=image.attrs['alt']
      # print(title)
    star=i.find('p')
    star=star['class'][1]
    # print(star)
    price=i.find('p',class_='price_color').text
    price=float(price[2:])
    # print(price)
    books.append([title, star , price ])

df=pd.DataFrame(books,columns=['Title', 'star-rating' ,'Price'])
print(df)

df.to_csv("books_data.csv",index=False)
df.to_excel("books_data.xlsx",index=False)