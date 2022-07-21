import requests as r


# SCARICARE & SALVARE UN FILE

res = r.get("https://www.google.com/images/branding/googlelogo/2x/googlelogo_light_color_272x92dp.png")

with open("google.png", "wb") as f:
    f.write(res.content)


# SCARICARE UNA PAGINA WEB

res = r.get("https://it.wikipedia.org/wiki/Python")
s = res.text


# PARSING DELLA PAGINA WEB

from bs4 import BeautifulSoup

s = BeautifulSoup(s)

for link in s.select("a"):
    print(link)

