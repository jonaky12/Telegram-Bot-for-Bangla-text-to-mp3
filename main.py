
import telebot
import asyncio

import edge_tts

# telegram bot api from botfather
API_KEY = '******' 
bot = telebot.TeleBot(API_KEY)

VOICE = "bn-BD-NabanitaNeural"
OUTPUT_FILE = "test.mp3"


async def _main(message) -> None:
    communicate = edge_tts.Communicate(message.text, VOICE)
    await communicate.save(OUTPUT_FILE)
    chat_id = message.chat.id
    document = open(OUTPUT_FILE, 'rb')
  
    try:
      bot.send_document(chat_id, document)
    except:
      bot.reply_to(message, "Generating failed")
      





@bot.message_handler(func=lambda message: True)
def echo_all(message):
    
    bot.reply_to(message, "Generating Audio")
    asyncio.run(_main(message))

bot.infinity_polling()
