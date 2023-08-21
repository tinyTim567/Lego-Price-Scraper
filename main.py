from datetime import datetime

from web_scraper.exporter import export_all_to_csv

url = "https://www.lego.com/en-gb/pick-and-build/pick-a-brick?perPage=400&system=LEGO&system=TECHNIC"
creation_date = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

if __name__ == '__main__':
    input(f"""\n\n\n\n
==================================================

    Lego Web Scraper

    Press Enter to continue...

==================================================
        """)

    print("\n\n\n\n\n\n")
    export_all_to_csv(url, creation_date)

    input(f"""\n\n\n\n\n\n
==================================================

    Finished scraping 
    Output saved to "output/{creation_date}.csv"

    Press Enter to exit

==================================================
    """)
