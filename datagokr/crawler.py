from bs4 import BeautifulSoup
import requests
import re

def get_data_api():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
    titlelist = []
    desclist = []
    linklist = []
    for page_num in range(1, 2):
        url = f"https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=&detailKeyword=&publicDataPk=&recmSe=N&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage={page_num}&perPage=10&brm=%EB%B3%B4%EA%B1%B4%EC%9D%98%EB%A3%8C&instt=%EA%B3%B5%EA%B3%B5%EA%B8%B0%EA%B4%80&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode="
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        # title crawling
        titles = soup.find_all("span", {"class":"title"})
        for title in titles:
            titlelist.append(title.text.strip())

        # desc crawling
        descs = soup.find_all("dd", {"class":"ellipsis"})
        for idx, desc in enumerate(descs):
            # 주요 설명아래 부가 설명으로 여러줄이 있을수 있어 주요 설명만 가지고 올수 있도록 \n으로 끊어서 첫번째 요소만 가져온다
            primary_desc = desc.text.strip().split("\n")[0]
            desclist.append(primary_desc)
            print(idx, ": ", desclist[idx])

        # link crawling
        links = [link['href'] for link in soup.find_all('a', href=True) if re.match(".*openapi\.do", link["href"])]
        for idx, addr in enumerate(links):
            linklist.append("http://www.data.go.kr"+addr)
            print(idx, linklist[idx])

    print("length: ", len(titlelist), len(desclist), len(linklist))

    for idx in range(len(titlelist)):
        print(idx, ":", titlelist[idx], " - ", desclist[idx], " - ", linklist[idx])
        f = open("apidata.csv", "a", -1, "utf-8")
        f.write(str(idx)+"\t"+titlelist[idx]+"\t"+desclist[idx]+"\t"+linklist[idx]+"\n")
        f.close()

def get_data_file():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
    title=[]
    desc=[]
    link_addr=[]
    for page_num in range(1, 48):
        url = f"https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=&detailKeyword=&publicDataPk=&recmSe=&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage={page_num}&perPage=10&brm=%EB%B3%B4%EA%B1%B4%EC%9D%98%EB%A3%8C&instt=%EA%B3%B5%EA%B3%B5%EA%B8%B0%EA%B4%80&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode="
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

        linkd = [link['href'] for link in soup.find_all('a', href=True)]
        for link_data in linkd:
            if re.match(".*fileData\.do", link_data):
                link_addr.append("http://www.data.go.kr"+link_data)

    print("length: ", len(title), len(desc), len(link_addr))

    for idx in range(len(title)):
        print(idx, ":", title[idx], " - ", desc[idx], " - ", link_addr[idx])
        f = open("filedata.csv", "a", -1, "utf-8")
        f.write(str(idx)+"\t"+title[idx]+"\t"+desc[idx]+"\t"+link_addr[idx]+"\n")
        f.close()

if __name__ =="__main__":
    # get_data_file()
    get_data_api()

