# Purpose: Test file for testing code snippets for get info from mal site

import requests
from bs4 import BeautifulSoup


def escape(list, str, strip=True):
    for escape in list:
        str = str.replace(escape, "")

    if strip:
        return str.strip()
    else:
        return str


ANIME_ID = 1
req = requests.get("https://myanimelist.net/anime/" + ANIME_ID, timeout=5)
soup = BeautifulSoup(req.text, "html.parser")

attribute = {
    "escape_list": (),
    "sibling_distance": 0,
    "search_key": "",
    # "first_list_index": 0,
    "list_jumper": 1,
}


if attribute.get("first_list_index") is None:
    val = escape(
        attribute.get("escape_list", ()),
        soup.find("span", string=attribute.get("search_key", ""))
        .parent.contents[attribute.get("sibling_distance", 0)]
        .string,
    )

else:
    val = []
    temp = soup.find("span", string=attribute.get("search_key", "")).parent.contents
    print(temp)
    for i in range(
        attribute.get("first_list_index", 0), len(temp), attribute.get("list_jumper", 1)
    ):
        val.append(temp[i].string)

print(val)
