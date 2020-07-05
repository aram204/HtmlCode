import requests
from bs4 import BeautifulSoup
html = requests.get("https://httpstatuses.com/")
soup = BeautifulSoup(html.content ,"html.parser")
html = soup.prettify()
with open('code2.html','w') as f:
    f.write(html)
li=""
for tag in soup.find_all("li"):
    li = li + tag.text.replace(" ", "-", 1) + "\n"
with open("liCode2.txt", "w") as f:
    f.write(li)