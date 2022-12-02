import requests
import re

url='https://www.edx.org/'
check =  []

r = requests.get(url)
html = r.text.encode("utf8")
search = re.findall(r'<a href=[\'"?](https[://\w\-._]+)', html.decode("utf8"))

for link in search:
    if link not in check:
        check.append(link)
        with open("link.txt","a") as file:
            file.write(f'{link}\n')

# print(html)
# comando: python .\crawlerexemplo.py
