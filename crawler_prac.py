# requests and bs4 - 웹페이지 읽어오고 빠르고 정적인 페이지 가능
# selenium - 웹페이지 자동화가능, 느이다, 스크롤을 내린다거나 로그인 해야 할때 등 동적인 페이지 가능
# user-agent - 프로그램을 통해서가 아닌 어떤 브라우를 통해서 접속했는지 가짜로 알려주기 위해

"""
크롤링의 가장 기본적인 사용법
headers ={'User-Agent':'브라우저 정보'}
url = "접속할싸이트"
requests.get(url=url, headers=headers)

"""

# 라이브러리 불러오기
import requests

#User-Agent값 넣기
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

#url주소 넣기
url = "https://www.mlb.com/stats/"

#get방식으로 소스 요청
r = requests.get(url=url, headers=headers)

#status코드가 200인 확인
print(r.status_code)

html_docs = requests.get("https://www.mlb.com/stats/", headers=headers)
print(html_docs.text)

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_docs.text, "html.parser")
span_set = soup.find_all("span")

print("############################################")
print(span_set)
print(len(span_set))
print("############################################")
for span in span_set:
    print(span.text)

html_docs = html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>"""

soup = BeautifulSoup(html_docs, "html.parser")

# 처음 나오는 p태그 방법1, soup.tag_name 방법2. soup.find('tag_name')
print(soup.p)
print(soup.find('p'))
# 처음 나오는 a태그의 href속성값 가져오기
print(soup.find('a')['href'])
print(soup.a['href'])