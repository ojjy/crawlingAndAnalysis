import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
response_data=requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716", headers=headers)


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
        movie = {'rank':int(rank), 'title':title, 'point':point}
        db.movie.insert_one(movie)

