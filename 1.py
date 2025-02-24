from flask import Flask, request, render_template_string
import pyperclip

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>اشتراک متن</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { 
            font-family: Arial; 
            padding: 20px;
            direction: rtl;
        }
        textarea {
            width: 100%;
            height: 200px;
            margin: 10px 0;
            padding: 10px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h2>انتقال متن به کامپیوتر</h2>
    <form method="POST">
        <textarea name="text" placeholder="متن خود را اینجا وارد کنید"></textarea><br>
        <button type="submit">ارسال</button>
    </form>
    {% if message %}
    <p style="color: green;">{{ message }}</p>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ''
    if request.method == 'POST':
        text = request.form.get('text', '')
        pyperclip.copy(text)
        message = 'متن با موفقیت در کلیپ‌بورد کپی شد!'
    return render_template_string(HTML_TEMPLATE, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)