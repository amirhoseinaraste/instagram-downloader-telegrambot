# define start command handler
from telebot import types

def register_handlers(bot):
    @bot.message_handler(commands = ['start'])
    def send_welcome(message):
        # welcome message 
        welcome_message = """

        👋 سلام! به *ربات دانلودگر رپکینگ* خوش اومدی!
                     
📥 من می‌تونم بهت کمک کنم تا *پست‌ها، ریلزها و استوری‌های اینستاگرام* رو فقط با ارسال لینک دانلود کنی!
                     
🔗 کافیه لینک محتوا رو بفرستی تا سریعاً محتوا رو بهت تحویل بدم.
        """

        bot.reply_to(message, welcome_message)