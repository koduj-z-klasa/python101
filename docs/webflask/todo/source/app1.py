import os
from flask import Flask, render_template, current_app
from db import init_app, init_db

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    SITE_NAME='Projekty Flask',
    DATABASE=os.path.join(app.root_path, 'db.sqlite')
))

init_app(app)

# rejestracja blueprintów


@app.route('/')
def index():
    # return 'Cześć, tu Python i Flask!'
    return render_template('index.html')

with app.app_context():
    if not os.path.exists(current_app.config['DATABASE']):
        init_db()
    if __name__ == "__main__":
        app.run(debug=True)
