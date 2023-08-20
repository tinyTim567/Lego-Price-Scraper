import csv

from web_scraper.scraper import get_item_list, is_last_page


def export_all_to_csv(url):
    i = 33
    item_list = []
    loop = True
    while loop:
        print(i)
        # Gets every item from current page
        url = url + "&page=" + str(i)
        item_list.clear()
        item_list = get_item_list(url)

        print(item_list)

        # Checks
        if is_last_page(url):
            loop = False
        else:
            i = i + 1

            # Writes items from page to file
            with open("output.csv", "a", newline="") as file:
                writer = csv.writer(file)

                writer.writerows(item_list)


def export_to_csv(url):
    item_list = get_item_list()

    with open("output.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerows(item_list)

    print("Done")
