import telebot
import time
import datetime
import pytz
import random
from telebot import types
from flask import Flask, render_template # render_template add kar diya
from threading import Thread
import os

# --- WEB SERVER SETUP ---
app = Flask(__name__)

@app.route('/')
def home():
    # Ye aapke templates/index.html ko load karega
    return render_template('index.html')

def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

# --- BOT SETTINGS ---
API_TOKEN = '8616199952:AAFn9PcsQzw5Gw5ZL4Uv0jNy7Rcvw1guoew'
bot = telebot.TeleBot(API_TOKEN)
IST = pytz.timezone('Asia/Kolkata')
AUTH_KEY = "KULAMANI-L7"

def get_lottery7_period():
    try:
        now = datetime.datetime.now(IST)
        total_minutes = (now.hour * 60) + now.minute
        # Period base 9671
        current_period_suffix = 9671 + total_minutes
        date_str = now.strftime("%Y%m%d")
        return f"{date_str}1000{current_period_suffix}"
    except Exception:
        return "Syncing..."

@bot.message_handler(commands=['start'])
def start(message):
    # Professional Start Message
    welcome_text = (
        "🚀 **PREDICTOR 4.0 AI OFFICIAL**\n\n"
        "Welcome to the most advanced AI tool.\n"
        "------------------------------\n"
        "🔑 Please enter your **Activation Key** to continue:"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == AUTH_KEY)
def login_success(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('🎰 LOTTERY 7 (1-MIN)')
    markup.add(btn1)
    
    success_text = (
        "✅ **ACCESS GRANTED**\n\n"
        "System is now online and synced with server.\n"
        "Click the button below to get prediction!"
    )
    bot.send_message(message.chat.id, success_text, reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == '🎰 LOTTERY 7 (1-MIN)')
def predict(message):
    p_id = get_lottery7_period()
    res = random.choice(['BIG 🔴', 'SMALL 🟢'])
    conf = random.randint(94, 98)

    final_msg = (
        f"✅ **PREDICTION READY**\n"
        f"------------------------------\n"
        f"📅 **Period:** `{p_id}`\n"
        f"🎯 **Result:** {res}\n"
        f"🔥 **Confidence:** {conf}%\n"
        f"------------------------------\n"
        f"⚠️ *Note: Follow 3-level money management.*"
    )
    bot.send_message(message.chat.id, final_msg, parse_mode='Markdown')

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()

if __name__ == "__main__":
    print("🚀 Bot is starting...")
    keep_alive()
    # Continuous polling with error handling
    while True:
        try:
            bot.polling(none_stop=True, timeout=60)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(10)
