import sqlite3
from contextlib import contextmanager

DATABASE_PATH = 'instance/pdb_analytics.db'

@contextmanager
def get_db_connection():
    """Automatically closes the database connection."""
    conn = sqlite3.connect(DATABASE_PATH)
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    """Creates the database tables."""
    with get_db_connection() as conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS most_viewed_proteins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pdb_id TEXT NOT NULL,
            title TEXT,
            views INTEGER,
            date_recorded DATE DEFAULT CURRENT_DATE,
            timeframe TEXT CHECK(timeframe IN ('daily', 'monthly'))
        )
        ''')
        conn.commit()

def save_proteins(data, timeframe):
    """Saves scraped data to the database."""
    with get_db_connection() as conn:
        for protein in data:
            conn.execute('''
            INSERT INTO most_viewed_proteins (pdb_id, title, views, timeframe)
            VALUES (?, ?, ?, ?)
            ''', (protein['pdb_id'], protein['title'], protein['views'], timeframe))
        conn.commit()

# Initialize the database when imported
init_db()