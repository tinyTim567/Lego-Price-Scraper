import csv

from web_scraper.scraper import get_item_list


def export_to_csv():
    item_list = get_item_list()

    with open("output.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerows(item_list)

    print("Done")
