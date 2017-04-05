import os
from flask import Flask


app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/<name>/")
def hello_name(name):
    return "Hello {0}!".format(name)


print("hi")

if __name__ == "__main__":
    app.run()
