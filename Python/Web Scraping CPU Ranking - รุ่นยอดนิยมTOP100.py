import requests
from bs4 import BeautifulSoup
import pandas as pd

#ดึงข้อมูล
url = "https://notebookspec.com/topchart/cpu.html"
res = requests.get(url)

# สกัดข้อมูล
soup = BeautifulSoup(res.text,"html.parser")
cpu = soup.find('ul', class_="top-100-list").find_all('li')

num = []
title = []
price = []

for i in cpu:
    num = i.find('div', class_='num').text.strip()
    title = i.find('div', class_='title').text.strip()
    price = i.find('div', class_='price').text.strip()
    print(num,title,price)

# เก็บข้อมูล
df.to_csv('mbTOP100.csv')

