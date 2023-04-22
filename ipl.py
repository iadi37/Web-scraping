import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.iplt20.com/auction/2023"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

# column=soup.find_all("div",class_='auction-grid-view mt-3')
names = soup.find_all("div", class_='agv-team-name')
team_name = []
for i in names:
    name = i.text
    team_name.append(name)
# print(team_name)
funds = soup.find_all("div", class_="avg-fund-remaining")
money = []
for i in funds:
    fund = i.text[18:].replace("\n", "").replace(",","")
    money.append(fund)
print(money)
overseas_player = []
over_pl = soup.find_all("ul", class_="mb-0 px-1")
for i in over_pl:
    abroad=i.text[18:][:2].replace("\n","")
    overseas_player.append(abroad)
# print(overseas_player)



# print(overseas_player)

total_player = []
total_pl = soup.find_all("li", class_="m-0 px-1")
for i in total_pl:
    name = i.text[14:].replace("\n","")
    total_player.append(name)
# print(total_player)

# for i in over_pl:
#     name = i.text[18:].replace("\n", "")
#     total_player.append(name)
# print(total_player)




#
# for i in funds:
#     fund=i.text
#     team_name.append(fund)
# # print(fund_remaining)
# #
df=pd.DataFrame({"Teams":team_name,"Money Left":money,"Overseas Player":overseas_player,"Total Player":total_player})
#
# df.to_csv("ipl2023.csv")
# df.to_excel("ipl2023.xlsx")
