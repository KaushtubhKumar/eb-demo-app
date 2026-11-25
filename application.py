import os
from flask import Flask
application = Flask(__name__)

@application.route("/")
def home():
    env = os.environ.get("APP_ENV", "not-set")
    ver = os.environ.get("APP_VERSION", "v1")
    return f"<h1 style='font-family:Arial;text-align:center;margin-top:80px'>Elastic Beanstalk - {ver}<br>Environment: {env}</h1>"

if __name__ == "__main__":
    application.run()
