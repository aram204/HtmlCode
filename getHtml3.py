import requests
from bs4 import BeautifulSoup
code = requests.get("https://httpstatuses.com/")
html = code.text
with open('code3.html','w') as f:
    f.write(html)
soup = BeautifulSoup(html,"html.parser")
li=""
for tag in soup.find_all("li"):
    li = li + tag.text.replace(" ", "-", 1) + "\n"
with open("liCode3.txt", "w") as f:
    f.write(li)