from bs4 import BeautifulSoup
import requests
import re


def get_web_page(url):
    result = requests.get(url)
    return BeautifulSoup(result.text, "html.parser")


def get_price_list():
    url = "https://www.lego.com/en-gb/pick-and-build/pick-a-brick?perPage=400&system=LEGO&system=TECHNIC"
    soup = get_web_page(url)

    # , class_="ElementsList_leaf_3tVNf"

    s = soup.find("main")
    s = s.find("div", class_="PickABrickPage_maxWidthContainer__h2uqW")
    s = s.find("div", class_="PickABrickPage_wrapper__3gMRD")
    s = s.find("div", id="pab-results-wrapper")
    s = s.find("div", class_="PickABrickPage_layout__B0a9f")
    s = s.find("div", class_="ElementsContainer_container__bBlaE")
    s = s.find("ul", class_="ElementsList_leaves__iT4F8")

    # print(s)

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
        print(item_name)
        print(item_id)
        print(item_price)

    return item_list
