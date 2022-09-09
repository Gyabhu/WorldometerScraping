
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
url = BeautifulSoup('https://www.worldometers.info/coronavirus/', 'html.parser')
soup = requests.get(url)
soup = soup.text
code = BeautifulSoup(soup, "lxml")
code = code.table
data = []
tags = code.find_all('tr')
for tag in tags:
  x = tag.text
  data.append(x)

datas = []
for i in data:
  datas.append(i.split('\n')[1:-1])
cleaned_data = [i for i in datas if i[0] != '']


file = open('covid_data2.csv','w')
x = csv.writer(file)
for i in cleaned_data:
  x.writerow(i)
file.close()


df = pd.read_csv('covid_data2.csv', encoding='unicode_escape')
print(df)
