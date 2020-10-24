import os, random, time
import telebot
#imports

workfolder = "/path/to/images/folder"
timetospeep = 60
token = "yourbottoken"
channelid = "yourchannelid"
#variables

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, я бот для автопостинга пикчей в Telegram канал, чтобы я начал высылать пикчи, отредактируй переменные в коде, добавь меня в админы канала, и выстави айди канала в коде.")

)
def send_post(message):
		pic = random.choice(os.listdir(workfolder))
		fullpath = (workfolder + pic	
	bot.send_photo(channelid, fullpath)
	time.sleep(timetospeep)

bot.polling()




