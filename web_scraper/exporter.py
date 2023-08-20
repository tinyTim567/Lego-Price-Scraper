import csv
from datetime import datetime

from web_scraper.scraper import get_item_list, is_last_page


def write_to_file(data):
    filename = f"output/{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.csv"

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerows(data)


def export_all_to_csv(url):
    i = 1
    item_list = []
    loop = True
    while loop:
        print(i)
        # Gets every item from current page
        url = url + "&page=" + str(i)
        item_list.clear()
        item_list = get_item_list(url)

        # Checks
        if is_last_page(url):
            loop = False
        else:
            i = i + 1

            write_to_file(item_list)


def export_to_csv(url):
    write_to_file(get_item_list(url))

    print("Done")
