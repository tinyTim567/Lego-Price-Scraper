from bs4 import BeautifulSoup
import requests


def get_web_page(url):
    result = requests.get(url)
    return BeautifulSoup(result.text, "html.parser")


def is_last_page(soup):
    s = soup.find("div", class_="ElementsShown_textWrapper__VQQ6C body-lg-regular")
    s = s.findAll("span")

    num = str(s[1].text).split()
    if int(num[3]) >= int(num[5]):
        return True
    else:
        return False


def get_item_list(soup):
    print("Done")
    print("Searching page...")

    s = soup.find("ul", class_="ElementsList_leaves__iT4F8")

    print("Getting item data...")

    item_list = []
    # item_list = [[name, id, price]]
    for item in s:
        item = item.find("div")
        item_name = ((item.find("button")).find("span", class_="ElementLeaf_elementTitle__xda82")).text
        item_id = item.find("span", class_="Text__BaseText-sc-13i1y3k-0 iEGSLL").text.lstrip("ID: ")
        item_price = item.find("div", class_="ElementLeaf_priceAndMaxQuantity__8Wb6Z").find("span").find(
            "span").text.lstrip("£")

        item = [item_name, item_id, item_price]
        item_list.append(item)

    print("Done")

    return item_list
