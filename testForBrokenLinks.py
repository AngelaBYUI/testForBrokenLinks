import pandas as pd
import requests
from bs4 import BeautifulSoup


#This file is for iterating the html to find the picture which will show as a broken link
# find the <span class="_advp _aeam"> -> <img class"_9vx6" src={the link below}> ->mark as broken
# broken link imgsrc="https://static.whatsapp.net/rsrc.php/v4/yB/r/_0dVljceIA5.png"

URL = "https://chat.whatsapp.com/Gnrh4YhWLwD6a43hl9YUaG"
response = requests.get(URL)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup)
first_layer_div=soup.find_all('div', class_="_2ywh _li _9kh2")
for div in first_layer_div:
    second_layer_div=div.find("div", class_="_2y_d _9rxy")
    for div2 in second_layer_div:
        third_layer_div=div2.find("div", class_="_9r_7")#Solved: Can't find the item in last layer, so goes to the next layer and solved
        if third_layer_div: #cuz the first item isn't what we want, so we need this line
            for div3 in third_layer_div:
                imgForLink=div3.find("img", class_="_9vx6") #tips: if you can't find section or id, try to find the next layer class, this is how it works
                if imgForLink and imgForLink.get("src") == "https://static.whatsapp.net/rsrc.php/v4/yB/r/_0dVljceIA5.png":
                    print("It's a broken link")
                else:
                    print(imgForLink)