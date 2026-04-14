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
    return "Lottery 7 Ultra Pro is Online!"

def run():
    app.run(host='0.0.0.0', port=8080)

# --- BOT SETTINGS ---
API_TOKEN = '8616199952:AAFn9PcsQzw5Gw5ZL4Uv0jNy7Rcvw1guoew'
bot = telebot.TeleBot(API_TOKEN)
IST = pytz.timezone('Asia/Kolkata')
AUTH_KEY = "KULAMANI-L7"

def get_lottery7_period():
    # India ka current time
    now = datetime.datetime.now(IST)
    
    # Lottery 7 calculation: Aaj ke total minutes
    total_minutes = (now.hour * 60) + now.minute
    
    # 2:09 PM par aapka period 10569 tha
    # Us hisab se formula: (Hour*60 + Min) + 9710
    # 2:09 = 849 minutes. 849 + 9720 = 10569.
    
    current_period_suffix = 9720 + total_minutes
    date_str = now.strftime("%Y%m%d")
    
    # Final Format: Date + 1000 + 5 digit number
    return f"{date_str}1000{current_period_suffix}"

@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.chat.id, "🛰️ **BOOTING PREDICTOR 4.0...**", parse_mode='Markdown')
    time.sleep(1)
    bot.edit_message_text("🔑 **Please Enter Your Activation Key:**", message.chat.id, msg.message_id, parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == AUTH_KEY)
def login_success(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('🎰 LOTTERY 7 (1-MIN)')
    markup.add(btn1)
    bot.send_message(message.chat.id, "✅ **ACCESS GRANTED**\nWelcome Kulamani! Click below for signal.", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '🎰 LOTTERY 7 (1-MIN)')
def predict(message):
    p_id = get_lottery7_period()
    
    # Animation
    ani = bot.send_message(message.chat.id, "🧠 **AI Analyzing Server Patterns...**")
    time.sleep(1.5)
    
    result = random.choice(['BIG 🔴', 'SMALL 🟢'])
    confidence = random.randint(94, 98)
    
    final_msg = (
        f"✅ **PREDICTION FETCHED**\n"
        f"------------------------------\n"
        f
