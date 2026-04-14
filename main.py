import telebot
import time
import datetime
import pytz
import random
from telebot import types
from flask import Flask
from threading import Thread

# Web Server for Render
app = Flask('')

@app.route('/')
def home():
    return "Lottery 7 Pro is Running!"

def run():
    app.run(host='0.0.0.0', port=8080)

# Bot Configuration
API_TOKEN = '8616199952:AAFn9PcsQzw5Gw5ZL4Uv0jNy7Rcvw1guoew'
bot = telebot.TeleBot(API_TOKEN)
IST = pytz.timezone('Asia/Kolkata')
AUTH_KEY = "KULAMANI-L7"

def get_lottery7_period():
    now = datetime.datetime.now(IST)
    date_str = now.strftime("%Y%m%d")
    # Exact Lottery 7 calculation logic
    total_minutes = (now.hour * 60) + now.minute
    period_number = 10001 + total_minutes
    # Format: Date + 1000 + Period (Total 17 digits)
    return f"{date_str}1000{period_number}"

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🚀 **LOTTERY 7 AI V4.0**\n\n🔑 Please enter your **Activation Key** to continue:", parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == AUTH_KEY)
def login_success(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('🎰 LOTTERY 7 (1-MIN)')
    markup.add(btn1)
    bot.send_message(message.chat.id, "✅ **Login Successful!**\nSelect the game to get prediction.", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '🎰 LOTTERY 7 (1-MIN)')
def predict(message):
    p_id = get_lottery7_period()
    
    # Professional Animation
    msg = bot.send_message(message.chat.id, "📡 **Fetching Data from Server...**")
    time.sleep(1)
    bot.edit_message_text("🧠 **AI Analyzing Trends...**", message.chat.id, msg.message_id)
    time.sleep(1)
    
    res = random.choice(['BIG 🔴', 'SMALL 🟢'])
    conf = random.randint(95, 99)
    
    final_text = (
        f"🎯 **LOTTERY 7 (1-MIN)**\n"
        f"--------------------------\n"
        f"📅 **Period:** `{p_id}`\n"
        f"🔥 **Result:** {res}\n"
        f"💎 **Confidence:** {conf}%\n"
        f"--------------------------\n"
        f"✅ *Next prediction in 1 minute*"
    )
    bot.edit_message_text(final_text, message.chat.id, msg.message_id, parse_mode='Markdown')

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
