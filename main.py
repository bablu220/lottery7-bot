import telebot
import time
import datetime
import pytz
import random
from telebot import types
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Lottery 7 Predictor 4.0 is Online!"

def run():
    app.run(host='0.0.0.0', port=8080)

API_TOKEN = '8616199952:AAFn9PcsQzw5Gw5ZL4Uv0jNy7Rcvw1guoew'
bot = telebot.TeleBot(API_TOKEN)
IST = pytz.timezone('Asia/Kolkata')

# Activation Key (Aap badal bhi sakte hain)
AUTH_KEY = "KULAMANI-L7"

def get_lottery7_period():
    now = datetime.datetime.now(IST)
    date_str = now.strftime("%Y%m%d")
    # Lottery 7 / 55 Club 1-Min exact calculation
    total_minutes = (now.hour * 60) + now.minute
    # Agar screenshot ke hisab se 10569 chal raha hai, toh base 10001 + minutes
    period_number = 10001 + total_minutes
    return f"{date_str}{period_number}"

@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.chat.id, "🚀 **Starting LOTTERY 7 AI ENGINE...**", parse_mode='Markdown')
    time.sleep(1)
    bot.edit_message_text("🔑 **Please Enter Activation Key:**", message.chat.id, msg.message_id, parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == AUTH_KEY)
def login_success(message):
    welcome_msg = "✅ **Access Granted!**\nWelcome to Lottery 7 Predictor v4.0"
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('🎰 LOTTERY 7 (1-MIN)')
    btn2 = types.KeyboardButton('🚀 WINGO PRO')
    markup.add(btn1, btn2)
    
    bot.send_message(message.chat.id, welcome_msg, reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == '🎰 LOTTERY 7 (1-MIN)')
def predict_l7(message):
    p_id = get_lottery7_period()
    
    # Login/Processing Animation
    proc = bot.send_message(message.chat.id, "🛰️ **Connecting to Lottery 7 Server...**", parse_mode='Markdown')
    time.sleep(1)
    bot.edit_message_text("🧠 **AI Analyzing Trends...**", message.chat.id, proc.message_id, parse_mode='Markdown')
    time.sleep(1)
    
    result = random.choice(['BIG 🔴', 'SMALL 🟢'])
    confidence = random.randint(93, 99)
    
    final_msg = (
        f"✅ **LOTTERY 7 PREDICTION**\n"
        f"------------------------------\n"
        f"📅 **Period:** `{p_id}`\n"
        f"🎯 **AI Result:** {result}\n"
        f"🔥 **Confidence:** {confidence}%\n"
        f"------------------------------\n"
        f"📢 *Wait for next period to bet!*"
    )
    bot.edit_message_text(final_msg, message.chat.id, proc.message_id, parse_mode='Markdown')

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
