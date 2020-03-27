import requests
import json
import os
from summary_form import *

IP = os.environ['HOST']
PORT = os.environ['PORT']
URL_ROOT = os.environ['URL_ROOT']
URL = 'http://' + IP + ':' + PORT + URL_ROOT + '/translate'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'



@app.route('/', methods=['GET', 'POST'])
def home():
    form = SummaryForm()
    summary = None
    if form.validate_on_submit():
        src = form.summarization.data.lower()
        headers = {"content-Tupe": "application/json"}
        data = [{"src":src, "id":100}]
        response = requests.post(URL, json=data, headers=headers)
        summary = response.text
        json_response = json.loads(summary)
        summary = json_response[0][0]['tgt']
    else:
        form.summarization.data = (' ')
    return render_template('home.html', form=form, translation=summary)
        
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
