# app.py
from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Bienvenue sur l'API ",
        "timestamp": datetime.datetime.now().isoformat()
    })

@app.route('/health ')
def health():
    return jsonify({
        " status ": " healthy ",
        " version ": " 1.0.0 "
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)