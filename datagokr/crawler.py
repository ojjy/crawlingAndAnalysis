from bs4 import BeautifulSoup
import requests
import re

def get_data_api():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
    title=[]
    desc=[]
    link_addr=[]
    for page_num in range(1, 15):
        url = f"https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=&detailKeyword=&publicDataPk=&recmSe=N&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage={page_num}&perPage=10&brm=%EB%B3%B4%EA%B1%B4%EC%9D%98%EB%A3%8C&instt=%EA%B3%B5%EA%B3%B5%EA%B8%B0%EA%B4%80&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode="
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        pre_titles = soup.find_all("span", {"class":"title"})
        for pre_title in pre_titles:
            title.append(pre_title.text.strip())
            # print(pre_title.text.strip())

        pre_descs = soup.find_all("dd", {"class":"ellipsis"})
        for pre_desc in pre_descs:
            desc.append(pre_desc.text.strip())
            # print(pre_desc.text.strip())
        # apiDataList > div.result-list > ul > li:nth-child(1) > dl > dt > a
        # link_str = soup.find_all(href=re.compile(("^\/data\/")))
        vals = [link['href'] for link in soup.find_all('a', href=True)]
        for value in vals:
            if re.match(".*openapi\.do", value):
                link_addr.append("http://www.data.go.kr"+value)
    print(len(title), len(desc))

    for idx in range(len(title)):
        print(idx, ":", title[idx], " - ", desc[idx], " - ", link_addr[idx])

    for idx in range(len(title)):
        print(idx, ": ", title[idx], " - ", desc[idx])
        f = open("apidata.csv", "a", -1, "utf-8")
        f.write(str(idx)+"\t"+title[idx]+"\t"+desc[idx]+"\t"+link_addr[idx]+"\n")
        f.close()

def get_data_file():

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
    title=[]
    desc=[]
    for page_num in range(1, 48):
        url = f"https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=&detailKeyword=&publicDataPk=&recmSe=&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage={page_num}&perPage=10&brm=%EB%B3%B4%EA%B1%B4%EC%9D%98%EB%A3%8C&instt=%EA%B3%B5%EA%B3%B5%EA%B8%B0%EA%B4%80&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode="
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        pre_titles = soup.find_all("span", {"class":"title"})
        for pre_title in pre_titles:
            title.append(pre_title.text.strip())
            print(pre_title.text.strip())

        pre_descs = soup.find_all("dd", {"class":"ellipsis"})
        for pre_desc in pre_descs:
            desc.append(pre_desc.text.strip())
            print(pre_desc.text.strip())
        # apiDataList > div.result-list > ul > li:nth-child(1) > dl > dt > a

        for link in soup.find('result-list').find_all('a', href=True):
            print("link", link['href'])
        print(len(title), len(desc))
        #
        # for idx in range(len(title)):
        #     print(idx, ": ", title[idx], " - ", desc[idx])
        #     f = open("datafile.csv", "a", -1, "utf-8")
        #     f.write(str(idx)+"\t"+title[idx]+"\t"+desc[idx]+"\n")
        #     f.close()


if __name__ =="__main__":
    get_data_file()
    get_data_api()
