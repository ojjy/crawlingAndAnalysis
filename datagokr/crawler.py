import urllib.request
from bs4 import BeautifulSoup

url = "https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=&detailKeyword=&publicDataPk=&recmSe=N&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage=1&perPage=10&brm=%EB%B3%B4%EA%B1%B4%EC%9D%98%EB%A3%8C&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode="
html = urllib.request.urlopen(url).read()
soup= BeautifulSoup(html, 'html.parser')

title = soup.findAll("span", {"class":"title"})

title_data=[]
print(len(title))
print(type(title))
for idx, title_name in enumerate(title):
    print(idx, ": ", title_name)
    str(title_name).replace('<span class="title">', "")
    print(title_name)