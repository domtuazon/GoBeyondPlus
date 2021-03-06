from flask import Flask, render_template
from flask_bower import Bower

app = Flask(__name__)
Bower(app)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    Bower(app)
    app.run(host='0.0.0.0')

