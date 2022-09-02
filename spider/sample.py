import requests
from bs4 import BeautifulSoup

link = "http://www.santostang.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
r = requests.get(link, headers=headers)
print(r.headers)

soup = BeautifulSoup(r.text, "html.parser")
title = soup.find_all("h1", "post-title")[0].a.text
print(title)

with open('title.txt', "a+") as f:
    f.write(title)
    f.close()
