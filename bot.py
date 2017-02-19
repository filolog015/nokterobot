# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_type=["text"])
def answerCho(message):
    bot.send_message(message.chat.id, "Чо?")

if __name__ == '__main__':
    bot.polling(none_stop=True)

# End
