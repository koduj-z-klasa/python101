from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Cześć, tu Python i Flask!'

with app.app_context():
    if __name__ == "__main__":
        app.run(debug=True)
