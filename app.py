from flask import Flask
import os
import logging
from datetime import datetime
from waitress import serve
from prometheus_flask_exporter import PrometheusMetrics

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info("flask_heroku_app", "an assignment for bytelearn", version="0.0.1")

@app.route("/")
def home_route():
    return "hello world"

@app.route("/time")
def time_route():
    return f"{datetime.now()}"

if __name__ == "__main__":
    if f"{os.environ.get('PROD')}".lower() == "true":
        serve(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        app.run(host="0.0.0.0",port=int(os.environ.get("PORT", 5000)))
