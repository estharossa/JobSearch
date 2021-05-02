from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    query = str(request.form.get('q'))
    url = 'https://jobs.github.com/positions.json?description=' + query
    req = requests.get(url)
    json_data = json.loads(req.content)
    return render_template('index.html', data=json_data)
