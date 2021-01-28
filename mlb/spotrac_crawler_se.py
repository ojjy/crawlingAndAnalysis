from selenium import webdriver

url = "https://www.spotrac.com/mlb/rankings/"

browser = webdriver.Chrome("./chromedriver")
browser.get(url)

rank=[]
name=[]
team=[]
extra=[]

for idx in range(1, 301):
    element = browser.find_element_by_xpath(f"//*[@id='main']/div[1]/div[3]/div/table/tbody/tr[{idx}]")
    print(element.text)
    str = element.text.split("\n")[0]
    if(str.isdigit()):
        rank.append(element.text.split("\n")[0])
        name.append(element.text.split("\n")[1])
        team.append(element.text.split("\n")[2])
        extra.append(element.text.split("\n")[3])
    else:
        rank.append(rank[idx-2])
        name.append(element.text.split("\n")[0])
        team.append(element.text.split("\n")[1])
        extra.append(element.text.split("\n")[2])



for i in range(0, 300):
    print(rank[i], " : ",name[i], " : ",team[i], " : ",extra[i])
