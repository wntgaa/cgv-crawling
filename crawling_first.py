import requests
import datetime
from bs4 import BeautifulSoup

d = datetime.datetime.now()
print (d.year,'년 ', d.month,'월 ', d.day,' 일')

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=d.yeard.monthd.day'
html = requests.get(url)
print(html.text)
