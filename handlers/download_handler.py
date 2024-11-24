# define content downloading handler
from services.instagram_service import download_instagram_content

def register_handler(bot):
    @bot.message_handler(func=lambda message: 'instagram.com' in message.text)
    def handle_instagram_link(message):
        link = message.text
        result, content_type = download_instagram_content(link)
         
        # if content does exist  return result otherwise throw not found error
        if result:
            #send content
            bot.send_document(message.chat.id, result)
        else:
            #error message
            error_message = """
❌ اوه! مشکلی پیش اومده.

به نظر می‌رسه لینک معتبری ارسال نکردی یا محتوا قابل دانلود نیست. لطفاً لینک رو دوباره بررسی کن.
"""
            # send error
            bot.send_message(message.chat.id, error_message)