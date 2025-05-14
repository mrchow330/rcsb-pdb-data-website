import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_most_viewed(timeframe='daily'):
    """Fetches most viewed PDB structures from RCSB."""
    url = f'https://www.rcsb.org/stats/most-viewed/{timeframe}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    table = soup.find('table', {'class': 'stats-table'})
    rows = table.find_all('tr')[1:]  # Skip header
    
    results = []
    for row in rows:
        cols = row.find_all('td')
        results.append({
            'pdb_id': cols[1].text.strip(),
            'title': cols[2].text.strip(),
            'views': int(cols[3].text.strip().replace(',', ''))
        })
    
    return results

# Test the function
if __name__ == '__main__':
    print(get_most_viewed('daily'))