import requests
from bs4 import BeautifulSoup
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)


def get_most_viewed(timeframe='daily'):
    url = f'https://www.rcsb.org/stats/most-viewed/{timeframe}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Parse the table - this selector might need adjustment
    table = soup.find('table', {'class': 'stats-table'})
    rows = table.find_all('tr')[1:]  # skip header

    results = []
    for row in rows:
        cols = row.find_all('td')
        results.append({
            'rank': cols[0].text.strip(),
            'pdb_id': cols[1].text.strip(),
            'title': cols[2].text.strip(),
            'views': cols[3].text.strip()
        })

    return results


@app.route('/api/most-viewed/<timeframe>')
def most_viewed(timeframe):
    return jsonify(get_most_viewed(timeframe))


if __name__ == '__main__':
    app.run()