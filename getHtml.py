import requests
html = requests.get("https://httpstatuses.com/")
a = html.content.decode("utf-8")
print(a)
with open('code.html','w') as f:
    f.write(a)



