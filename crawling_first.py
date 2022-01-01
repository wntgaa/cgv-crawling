import requests
import datetime
from bs4 import BeautifulSoup

d = datetime.datetime.now()
print (d.year,'년 ', d.month,'월 ', d.day,' 일' , '용산 아이파크몰 CGV')

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=d.yeard.monthd.day'
html = requests.get(url)
#print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')
title_list = soup.select('div.info-movie')

for i in title_list:
    print(i.select_one('a > strong').text.strip())

imax = soup.select_one('span.imax')
if (imax):
    imax = imax.find_parent('div', class_='col-times')
    title = imax.select_one('div.info-movie > a > strong').text.strip()
    print( '\n지금 상영중인 IMAX 영화는.' + title +'입니다.')

else:
    print('\nIMAX영화가 상영중이지 않습니다.')
