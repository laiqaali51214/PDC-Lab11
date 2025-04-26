from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

SOLR_URL = 'http://localhost:8983/solr/Laiqa-Ali_shard1_replica_n1/select'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')

    # Match all if query is empty
    solr_query = f'title:*{query}* OR author:*{query}* OR id:*{query}*'

    params = {
        'q': solr_query,
        'wt': 'json',
        'rows': 9
    }

    response = requests.get(SOLR_URL, params=params)
    data = response.json()
    docs = data['response']['docs']

    return jsonify(docs)

if __name__ == '__main__':
    app.run(debug=True)
