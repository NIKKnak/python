#
# # Напишите программу, удаляющую из текста все слова, содержащие "абв"
# import telebot
#
# def text_clear(text, find_str):
# 	ch = text.split()
# 	for item in ch:
# 		if item.find(find_str) > -1:
# 			ch.remove(item)
# 	return ' '.join(ch)
#
# bot = telebot.TeleBot("5844080573:AAHSieG0eid-fLZ8bylvMgUF0qJXFHaW-gE")
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")
#
# print("Запустился")
#
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message,text_clear(message.text,"абв"))
#
# bot.infinity_polling()
# message: True

#####################################################################
# Код преподавателя

# import telebot
#
# def del_abv(text):
# 	text = text.split(' ')
# 	return ' '.join([i for i in text if 'абв' not in i])
#
#
# bot = telebot.TeleBot("токен")
#
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.send_message(message.chat.id, del_abv(message.text))
#
#
# bot.infinity_polling()

#####################################################################