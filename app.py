import json

import requests
from flask import Flask, request, render_template

from actions.actions import ActionClientQuery

app = Flask(__name__, template_folder='Templates')
context_set: ""
actions = ActionClientQuery()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        val = request.form.get('text')
        data = json.dumps({"sender": "Rasa", "message": val})
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        res = requests.post('http://localhost:5005/webhooks/rest/webhook', data=data, headers=headers)
        res = res.json()
        val = res[0].get('text')
    else:
        val = ''
    return render_template('index.html', val=val)


if __name__ == '__main__':
    app.run(debug=True)
