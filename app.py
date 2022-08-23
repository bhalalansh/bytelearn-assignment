from flask import Flask
import os
from datetime import datetime
from waitress import serve


app = Flask(__name__)

@app.route("/")
def home_route():
    return "hello world"

@app.route("/time")
def time_route():
    return f"{datetime.now()}"

if __name__ == "__main__":
    if os.environ.get("PROD").lower() == "true":
        serve(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        app.run(host="0.0.0.0",port=int(os.environ.get("PORT", 5000)), debug=True)
