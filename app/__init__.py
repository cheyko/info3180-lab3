from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cheyko'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = 'e146f5150c1c0f'
app.config['MAIL_PASSWORD'] = '2e0bb8289b32ac'
mail = Mail(app)
from app import views