from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.yelp.com/biz/milk-and-cream-cereal-bar-new-york?osq=Ice+Cream'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

#User

us = soup.find_all('a', class_='lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE')

user = list()

cont = 0
for i in us:
    if cont < 12:
        user.append(i.text)
    else:
        break
    cont += 1


comt = soup.find_all('span', class_='lemon--span__373c0__3997G raw__373c0__3rKqk')

comentarios = list()

cont = 0
for i in comt:
    if cont < 12:
        comentarios.append(i.text)
    else:
        break
    cont += 1

df = pd.DataFrame({'Usuarios': user, 'Comentarios': comentarios}, index=list(range(2,14)))

print(df)