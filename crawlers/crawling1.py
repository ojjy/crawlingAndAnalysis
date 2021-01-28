import requests
from bs4 import BeautifulSoup


# response_data=requests.get("http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99")
# jsondata=response_data.json()
# gu_infos=jsondata['RealtimeCityAir']['row']
# for(idx = 0; idx < gu_infos.length):


# 파이썬으로 가져오지만 서버 입장에서 브라우저를 통해서 가져오는 것 처럼 행동
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
response_data=requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716", headers=headers)
# print(type(reponse_data))

# print(reponse_data.text)


soup = BeautifulSoup(response_data.text, "html.parser")
print(soup.text)
title = soup.select_one("#old_content > table > tbody > tr:nth-child(2) > td.title > div > a")
rows=soup.select("#old_content > table > tbody > tr")
print(rows)
for row in rows:
    a_tag = row.select_one(".title a")
#    print(a_tag.text)
    if a_tag is not None:
        title = a_tag.text
        rank = row.select_one('.ac img')['alt']
        point = row.select_one('.point').text
        print(int(rank), title, point)

