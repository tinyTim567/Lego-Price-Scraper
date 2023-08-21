import csv

from web_scraper.scraper import get_item_list, is_last_page, get_web_page


def write_to_file(data, creation_date):
    filename = f"output/{creation_date}.csv"

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)

        for row in data:
            writer.writerow(row)


def export_all_to_csv(page_url, creation_date):
    i = 1
    item_list = []
    loop = True
    while loop:
        print("--------------------------------------------------")
        print(f"Downloading page {i}...")
        # Gets every item from current page
        url = page_url + "&page=" + str(i)

        soup = get_web_page(url)
        soup = soup.find("main")

        if is_last_page(soup):
            loop = False

        item_list.clear()
        item_list = get_item_list(soup)

        print(f"Writing data from page {i} to file...")
        i = i + 1
        write_to_file(item_list, creation_date)
        print("Done")


def export_to_csv(url):
    write_to_file(get_item_list(url))

    print("Done")
