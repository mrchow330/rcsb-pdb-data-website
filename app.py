from flask import Flask, render_template
from database import get_db_connection
import scraper

app = Flask(__name__)

@app.route('/')
def dashboard():
    """Renders the analytics dashboard."""
    with get_db_connection() as conn:
        # Get today's top 10 proteins
        daily_proteins = conn.execute('''
        SELECT pdb_id, title, views 
        FROM most_viewed_proteins 
        WHERE timeframe = 'daily' 
        ORDER BY views DESC 
        LIMIT 10
        ''').fetchall()

        # Get monthly submission trend (example)
        trends = conn.execute('''
        SELECT date_recorded, COUNT(*) as submissions
        FROM most_viewed_proteins
        GROUP BY date_recorded
        ''').fetchall()

    return render_template('dashboard.html', 
                         daily_proteins=daily_proteins,
                         trends=trends)

if __name__ == '__main__':
    app.run(debug=True)