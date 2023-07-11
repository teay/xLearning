import requests
from bs4 import BeautifulSoup
import pandas as pd

#ดึงข้อมูล
url = "https://notebookspec.com/topchart/mainboard.html"
res = requests.get(url)

# สกัดข้อมูล
soup = BeautifulSoup(res.text,"html.parser")
mb = soup.find('ul', class_="top-100-list").find_all('li')

numls = []
titlels = []
pricels = []

for i in mb:
    num = i.find('div', class_='num').text
    title = i.find('div', class_='title').text.strip()
    price = i.find('div', class_='price').text.strip()
    numls.append(num)
    titlels.append(title)
    pricels.append(price)
    print(num,title,price)

# เก็บข้อมูล
df = pd.DataFrame({'อันดับ': numls, 'รุ่นMB': titlels, 'ราคา': pricels})
df.to_csv('TOP100MB.csv')
df.to_excel('TOP100MB.xlsx')
print("complete")
print("############################################################")



import requests
from bs4 import BeautifulSoup
import pandas as pd

#ดึงข้อมูล
url = "https://notebookspec.com/topchart/cpu.html"
res = requests.get(url)

# สกัดข้อมูล
soup = BeautifulSoup(res.text,"html.parser")
cpu = soup.find('ul', class_="top-100-list").find_all('li')

numls = []
titlels = []
pricels = []

for i in cpu:
    num = i.find('div', class_='num').text
    title = i.find('div', class_='title').text.strip()
    price = i.find('div', class_='price').text.strip()
    numls.append(num)
    titlels.append(title)
    pricels.append(price)
    print(num,title,price)

# เก็บข้อมูล
df = pd.DataFrame({'อันดับ': numls, 'รุ่นCPU': titlels, 'ราคา': pricels})
df.to_csv('TOP100CPU.csv')
df.to_excel('TOP100CPU.xlsx')
print("complete")
print("############################################################")



import requests
from bs4 import BeautifulSoup
import pandas as pd

#ดึงข้อมูล
url = "https://notebookspec.com/topchart/vga.html"
res = requests.get(url)

# สกัดข้อมูล
soup = BeautifulSoup(res.text,"html.parser")
vga = soup.find('ul', class_="top-100-list").find_all('li')

numls = []
titlels = []
pricels = []

for i in vga:
    num = i.find('div', class_='num').text
    title = i.find('div', class_='title').text.strip()
    price = i.find('div', class_='price').text.strip()
    numls.append(num)
    titlels.append(title)
    pricels.append(price)
    print(num,title,price)

# เก็บข้อมูล
df = pd.DataFrame({'อันดับ': numls, 'รุ่นVGA': titlels, 'ราคา': pricels})
df.to_csv('TOP100VGA.csv')
df.to_excel('TOP100VGA.xlsx')
print("complete")
print("############################################################")



import requests
from bs4 import BeautifulSoup
import pandas as pd

#ดึงข้อมูล
url = "https://notebookspec.com/topchart/ram.html"
res = requests.get(url)

# สกัดข้อมูล
soup = BeautifulSoup(res.text,"html.parser")
ram = soup.find('ul', class_="top-100-list").find_all('li')

numls = []
titlels = []
pricels = []

for i in ram:
    num = i.find('div', class_='num').text
    title = i.find('div', class_='title').text.strip()
    price = i.find('div', class_='price').text.strip()
    numls.append(num)
    titlels.append(title)
    pricels.append(price)
    print(num,title,price)

# เก็บข้อมูล
df = pd.DataFrame({'อันดับ': numls, 'รุ่นRAM': titlels, 'ราคา': pricels})
df.to_csv('TOP100RAM.csv')
df.to_excel('TOP100RAM.xlsx')
print("complete")
print("############################################################")



