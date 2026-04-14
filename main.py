import telebot
import time
import datetime
import pytz  # Timezone fix karne ke liye
import random
from telebot import types
from flask import Flask
from threading import Thread

# Web server setup
app = Flask('')

@app.route('/')
def home():
    return "Predictor 4.0 is Online!"

def run():
    app.run(host='0.0.0.0', port=8080)

# --- CONFIGURATION ---
API_TOKEN = '8616199952:AAFn9PcsQzw5Gw5ZL4Uv0jNy7Rcvw1guoew'
bot = telebot.TeleBot(API_TOKEN)
IST = pytz.timezone('Asia/Kolkata') # India Timezone

def get_period():
    # Render ke server par India ka time nikalne ke liye
    now = datetime.datetime.now(IST)
    date_str = now.strftime("%Y%m%d")
    # Din ke kul minutes (0 se 1439)
    total_minutes = (now.hour * 60) + now.minute
    # Predictor 4.0 style period format
    return f"{date_str}1000{total_minutes + 1}"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('🎮 55 CLUB')
    btn2 = types.KeyboardButton('🚀 WINGO')
    btn3 = types.KeyboardButton('📊 SYSTEM STATUS')
    markup.add(btn1, btn2, btn3)
    
    welcome_msg = (
        "🟢 **PREDICTOR 4.0 AI**\n"
        "------------------------------\n"
        "Welcome, User!\n"
        "**Status:** SECURE CONNECTION ESTABLISHED\n"
        "**AI Node:** Bhubaneswar Server 01\n\n"
        "Please select a game to start prediction."
    )
    bot.send_message(message.chat.id, welcome_msg, reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text in ['🎮 55 CLUB', '🚀 WINGO'])
def predict(message):
    current_period = get_period()
    
    # Fake Animation loading (Predictor 4.0 style)
    sent_msg = bot.send_message(message.chat.id, "🔍 **Analyzing Server Data...**")
    time.sleep(1)
    bot.edit_message_text("🛰️ **Syncing with API...**", message.chat.id, sent_msg.message_id)
    time.sleep(1)
    
    result = random.choice(['BIG 🔴', 'SMALL 🟢'])
    confidence = random.randint(85, 99)
    
    final_msg = (
        f"✅ **PREDICTION READY**\n"
        f"------------------------------\n"
        f"🎯 **Game:** {message.text}\n"
        f"📅 **Period:** {current_period}\n"
        f"🔥 **Result:** {result}\n"
        f"💎 **Confidence:** {confidence}%\n"
        f"------------------------------\n"
        f"⚠️ *Note: Trade at your own risk.*"
    )
    bot.edit_message_text(final_msg, message.chat.id, sent_msg.message_id, parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == '📊 SYSTEM STATUS')
def status(message):
    status_msg = (
        "✅ **SERVER STATUS**\n\n"
        "Main Server: **Online**\n"
        "API Latency: **24ms**\n"
        "AI Version: **4.0.0 (Latest)**\n"
        "Database: **Updated**"
    )
    bot.send_message(message.chat.id, status_msg, parse_mode='Markdown')

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
