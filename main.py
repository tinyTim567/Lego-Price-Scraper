from datetime import datetime
from packaging import version
import metadata

import requests

from web_scraper.exporter import export_all_to_csv

url = "https://www.lego.com/en-gb/pick-and-build/pick-a-brick?perPage=400&system=LEGO&system=TECHNIC"
creation_date = datetime.now().strftime('%Y-%m-%d %H-%M-%S')


def check_for_updates():
    response = requests.get("https://api.github.com/repos/tinyTim567/Lego-Price-Scraper/releases/latest")

    if response.status_code != 200:
        return "An error has occurred while checking for updates"
    else:
        print(response.json()["tag_name"])
        latest_version = response.json()["tag_name"]
        if version.parse(metadata.version) < version.parse(latest_version):
            return (f"Version {metadata.version} \n"
                    f"      A new version is available ({latest_version}) from: \n"
                    f"      https://github.com/tinyTim567/Lego-Price-Scraper/releases/latest")
        else:
            return f"Version {metadata.version} (latest)"


if __name__ == '__main__':
    input(f"""\n\n\n\n
==================================================

    Lego Web Scraper
    {check_for_updates()}
    
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
