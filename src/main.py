# src/main.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Function to serve as entry point for GCF
def main(request):
    return app(request)