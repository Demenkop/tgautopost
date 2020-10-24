import os, random, time
import telebot
#imports

workfolder = "/path/to/your/folder" #полный путь к папке
timetospeep = 1800 #промежуток между постами в секундах
token = "" #Токен бота
channelid = "" #айди канала где бот в админах
#variables

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, я бот для автопостинга пикчей в Telegram канал, чтобы я начал высылать пикчи, отредактируй переменные в коде, добавь меня в админы канала, и выстави айди канала в коде.")

while True:
	if len(os.listdir(workfolder)) == 0:
		time.sleep(timetospeep) # comment to check every second
		return
	pic = random.choice(os.listdir(workfolder))
	fullpath = (workfolder + "/" + pic)
	photo = open(fullpath, 'rb')
	bot.send_photo(channelid, photo)
	os.remove(fullpath)
	time.sleep(timetospeep)

bot.polling()
