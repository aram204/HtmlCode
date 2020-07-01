import requests
from bs4 import BeautifulSoup
html = requests.get("https://httpstatuses.com/")
a = html.content.decode("utf-8")
with open('code.html','w') as f:
    f.write(a)
soup = BeautifulSoup(html.text)
for tag in soup.find_all("li"):
    print(tag.text)



