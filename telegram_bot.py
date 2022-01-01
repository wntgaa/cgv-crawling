import telegram

bot = telegram.Bot(token = '5033818734:AAFR8CQsZAvd1WsCqHNTD3MsTd8bMHdb3Vw')

#for i in bot.getUpdates():
#    print(i.message)

bot.sendMessage(chat_id= 1703921842, text = "테스트 입니다.")
