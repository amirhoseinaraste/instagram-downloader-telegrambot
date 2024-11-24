import telebot
#from config import TOKEN
from handlers import start_handler, download_handler

TOKEN = '7630825069:AAHKomMKF3aef4jQ2txDB-PXfkQft_mchN8'

# Defining and setup a bot
bot = telebot.TeleBot(TOKEN)

# define handlers
start_handler.register_handlers(bot)
download_handler.register_handler(bot)

# start Polling
bot.polling()