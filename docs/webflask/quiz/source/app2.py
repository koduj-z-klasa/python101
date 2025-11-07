from flask import Flask, render_template

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY='bradzosekretnawartosc',
    SITE_NAME='Quiz Python'
))

@app.route('/')
def index():
    # return 'Cześć, tu Python i Flask!'
    return render_template('index.html')

with app.app_context():
    if __name__ == "__main__":
        app.run(debug=True)
