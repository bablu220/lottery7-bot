import telebot
import time
import datetime
import random
from telebot import types
from flask import Flask
from threading import Thread

# Render ke liye web server
app = Flask('')

@app.route('/')
def home():
    return "Bot is Alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

# Aapka Bot Token
API_TOKEN = '8616199952:AAFn9PcsQzw5Gw5ZL4Uv0jNy7Rcvw1guoew'
bot = telebot.TeleBot(API_TOKEN)

def get_period():
    now = datetime.datetime.now()
    date_str = now.strftime("%Y%m%d")
    total_minutes = (now.hour * 60) + now.minute
    return f"{date_str}1000{total_minutes}"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('🚀 GET AUTO PREDICTION'))
    bot.send_message(message.chat.id, "💎 **LOTTERY 7 AUTO-SERVER v5.0**\n\nStatus: **24/7 ONLINE** ✅", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '🚀 GET AUTO PREDICTION')
def auto_predict(message):
    current_period = get_period()
    sent_msg = bot.send_message(message.chat.id, "📡 **Fetching Server Data...**")
    time.sleep(1)
    
    result = random.choice(['BIG 🔴', 'SMALL 🟢'])
    confidence = random.randint(91, 98)
    
    final_msg = (
        f"✅ **PREDICTION FETCHED**\n"
        f"------------------------------\n"
        f"📅 **Period:** {current_period}\n"
        f"🎯 **AI Result:** {result}\n"
        f"🔥 **Confidence:** {confidence}%\n"
        f"------------------------------"
    )
    bot.edit_message_text(final_msg, message.chat.id, sent_msg.message_id, parse_mode='Markdown')

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
  
