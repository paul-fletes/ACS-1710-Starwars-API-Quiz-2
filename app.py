import json
import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    pass


@app.route('/results')
def results():
    pass


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True, port=3000)
