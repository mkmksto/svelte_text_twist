from flask import Flask
from flask_cors import cross_origin

app = Flask(__name__)


@app.route("/api")
def index():
    return "Api Root"


if __name__ == "__main__":
    app.run(debug=True)
