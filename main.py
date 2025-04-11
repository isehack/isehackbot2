
import telebot

TOKEN = '7807395933:AAFtsYTkiTHUGilo_T3c1i94qxEC55o594E'
bot = telebot.TeleBot(TOKEN)

# صورة الجمجمة
skull_image_url = 'https://i.ibb.co/Jkb6S4X/skull-warning.png'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_photo(
        message.chat.id,
        skull_image_url,
        caption='''
زوج: EUR/USD OTC
الاتجاه: هبوط
المدة: دقيقة واحدة
التحليل: كسر مقاومة قوية مع تأكيد من مؤشر RSI وتشبّع شرائي.
ملاحظة: ادخل الصفقة بعد دقيقة واحدة.
        '''
    )

bot.infinity_polling()
