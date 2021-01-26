from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

number = []
name = []
age = []
nationality = []
position = []
team = []
market_val = []

for page_num in range(1, 3):
    url = f"https://www.transfermarkt.com/marktwertetop/wertvollstespieler?ajax=yw1&page={page_num}"

    r = requests.get(url=url, headers=headers)

    #r.content대신, r.text도 가능
    soup = BeautifulSoup(r.content, 'html.parser')

    # 선수들의 정보가 담긴 태그와 클래스 찾기
    player_info = soup.find_all("tr", {"class":["even", "odd"]})

    # 첫번째 선수 정보
    print(player_info[0])

    #선수 정보 갯수
    print(len(player_info))



    for info in player_info:
        player = info.find_all("td")
        # print(player, "\n")
        # print(player[0])
        # 해당 정보를 찾아 각 리스트에 append
        number.append(player[0].text)
        name.append(player[3].text)
        position.append(player[4].text)
        age.append(player[5].text)
        nationality.append(player[6].find('img')['alt']) #==player[6].img['alt']
        team.append(player[7].img['alt'])
        market_val.append(player[8].text.strip()) #strip은 빈공간 제거
    print(number)
    print(name)
    print(position)
    print(age)
    print(nationality)
    print(team)
    print(market_val)

import pandas as pd

df = pd.DataFrame(
    {"number":number,
     "name":name,
     "position":position,
     "nationality":nationality,
     "age":age,
     "team":team,
     "market_val":market_val
     }
)
print(df)
# dataframe을 csv 파로 만들기

df.to_csv("soccer_player_info.csv", index=False)

# 두번째 페이지도 크롤링해서 50위까지 데이터 저장
