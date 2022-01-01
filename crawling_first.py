import requests
import datetime
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler
from bs4 import BeautifulSoup
bot = telegram.Bot(token = '')
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=d.yeard.monthd.day'


def job_function():
    d = datetime.datetime.now()
    print (d.year,'년 ', d.month,'월 ', d.day,' 일' , '용산 아이파크몰 CGV IMAX 상영작 알림')

    html = requests.get(url)
    #print(html.text)

    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')
    if (imax):
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id= 1703921842, text =  '용산 아이파크몰 CGV' + '\n지금 상영중인 IMAX 영화는' + title +'입니다.')
        #print( '\n지금 상영중인 IMAX 영화는.' + title +'입니다.')
        sched.pause()

sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=43200)
sched.start()
