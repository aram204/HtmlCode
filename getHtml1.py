import requests
from bs4 import BeautifulSoup
html = requests.get("https://httpstatuses.com/")
code = html.content.decode("utf-8")
with open('code1.html','w') as f:
    f.write(code)
soup = BeautifulSoup(html.text,"html.parser")
li=""
for tag in soup.find_all("li"):
    li=li+tag.text.replace(" ","-",1)+"\n"
with open("liCode1.txt", "w") as f:
    f.write(li)



