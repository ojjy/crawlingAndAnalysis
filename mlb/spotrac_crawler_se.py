from selenium import webdriver

url = "https://www.spotrac.com/mlb/rankings/"

browser = webdriver.Chrome("./chromedriver")
browser.get(url)
player_num=547
rank=[]
name=[]
team=[]
extra=[]
position=[]
age=[]
salary=[]

for idx in range(1, player_num+1):
    element = browser.find_element_by_xpath(f"//*[@id='main']/div[1]/div[3]/div/table/tbody/tr[{idx}]")
    print(element.text)
    str = element.text.split("\n")[0]
    if(str.isdigit()): # 동률이 없을때, 첫번째값이 순위
        rank.append(element.text.split("\n")[0])
        name.append(element.text.split("\n")[1])
        team.append(element.text.split("\n")[2])
        extra.append(element.text.split("\n")[3])

    else: #동률이 있을때 숫자가 빠지므로 첫번째 값은 이름
        rank.append(rank[idx-2]) # rank는 앞선수와 동일
        name.append(element.text.split("\n")[0])
        team.append(element.text.split("\n")[1])
        extra.append(element.text.split("\n")[2])

    position.append(extra[idx-1].split(" ")[0])
    age.append(extra[idx-1].split(" ")[1])
    salary.append(extra[idx-1].split(" ")[2])
    salary[idx-1]=salary[idx-1].replace('$', '')
    salary[idx-1]=salary[idx-1].replace(',', '')



for i in range(0, player_num):
    print(rank[i], " : ",name[i], " : ",team[i], " : ",position[i], " : ",age[i], " : ",salary[i])


import pandas as pd

mlb_df = pd.DataFrame(
    {
        "salary_rank":rank,
        "name":name,
        "team":team,
        "position":position,
        "age":age,
        "salary":salary
    }
)

mlb_df.to_csv("mlb_player_info.csv", index=False)