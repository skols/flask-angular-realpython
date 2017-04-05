import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Has to be after app is defined
from models import Result


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/<name>/")
def hello_name(name):
    return "Hello {0}!".format(name)


if __name__ == "__main__":
    app.run()
