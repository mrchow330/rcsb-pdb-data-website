import logging
from datetime import datetime
from scraper import get_most_viewed
from database import save_proteins

# Set up logging
logging.basicConfig(
    filename='C:/Windows/System32/GitBash/rcsb-pdb-data-website/scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def main():
    try:
        logging.info("Starting PDB scraper...")
        daily_data = get_most_viewed('daily')
        save_proteins(daily_data, 'daily')
        logging.info(f"Success! Saved {len(daily_data)} entries.")
    except Exception as e:
        logging.error(f"FAILED: {str(e)}")

if __name__ == '__main__':
    main()