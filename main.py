from web_scraper.exporter import export_all_to_csv, export_to_csv
from web_scraper.scraper import is_last_page

url = "https://www.lego.com/en-gb/pick-and-build/pick-a-brick?perPage=400&system=LEGO&system=TECHNIC"

if __name__ == '__main__':
    export_all_to_csv(url)
