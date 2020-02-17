import pyowm
import telebot

owm = pyowm.OWM('a86b011a4719480360159e0d15d14717', language = "ru") 
bot = telebot.TeleBot("1083081265:AAH9e-mt3urCNW2_G5TdvZA0EvJ93-IaYmI")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]

	answer = "В городе(стране) " + message.text + " сейчас " + w.get_detailed_status() + "\n"
	answer += "Температура сейчас в районе " + str(temp) + "\n\n"


	if temp < 10:
		print("Одевайтесь по-теплее!")
	elif temp < 20:
		print("Стоит что-нибудь накинуть на себя.")
	else:
		print("Погода просто класс!")

	bot.send_message(message.chat.id, answer)
bot.polling(none_stop = True )