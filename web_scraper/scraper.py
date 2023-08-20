from bs4 import BeautifulSoup
import requests


def get_web_page(url):
    result = requests.get(url)
    return BeautifulSoup(result.text, "html.parser")


def is_last_page(url):
    soup = get_web_page(url)

    s = soup.find("main")
    s = s.find("div", class_="ElementsShown_textWrapper__VQQ6C body-lg-regular")
    s = s.findAll("span")
    print(s)
    print(s[0])
    print(s[1])

    num = str(s[1].text).split()
    if num[3] == num[5]:
        return True
    else:
        return False


def get_item_list(url):
    soup = get_web_page(url)

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

    return item_list
