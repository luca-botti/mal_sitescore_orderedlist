import requests
import xmltodict
import json
import concurrent.futures
from bs4 import BeautifulSoup


# PARAMETERS
USE_MULTITHREADING = True
MAX_WORKERS = 5

FILE_NAME = ""


# CONSTANTS (DO NOT CHANGE)
COSTANT = {
    "web_link_start": "https://myanimelist.net/anime/",
    "anime_attributes": [
        {
            "string": "ANIME NAME",
            "xml": "series_title",
            "json": "anime_name",
        },
        {
            "string": "ANIME ID",
            "xml": "series_animedb_id",
            "json": "anime_id",
        },
        {
            "string": "ANIME SCORE",
            "json": "anime_score",
            "search_key": "Score:",
            "sibling_distance": 3,
        },
        {
            "string": "ANIME RANK",
            "json": "anime_rank",
            "escape_list": ("#", "\n"),
            "search_key": "Ranked:",
            "sibling_distance": 2,
        },
        {
            "string": "ANIME POPULARITY",
            "json": "anime_popularity",
            "escape_list": ("#", "\n"),
            "search_key": "Popularity:",
            "sibling_distance": 2,
        },
        {
            "string": "ANIME MEMBERS",
            "json": "anime_members",
            "escape_list": (",", "\n"),
            "search_key": "Members:",
            "sibling_distance": 2,
        },
        {
            "string": "ANIME FAVORITES",
            "json": "anime_favorites",
            "escape_list": (",", "\n"),
            "search_key": "Favorites:",
            "sibling_distance": 2,
        },
        {
            "string": "ANIME TYPE",
            "xml": "series_type",
            "json": "anime_type",
            "search_key": "Type:",
            "sibling_distance": 3,
        },
        {
            "string": "ANIME EPISODES",
            "xml": "series_episodes",
            "json": "anime_episodes",
            "escape_list": ("\n"),
            "search_key": "Episodes:",
            "sibling_distance": 2,
        },
        {
            "string": "ANIME STATUS",
            "json": "anime_status",
            "escape_list": ("\n"),
            "search_key": "Status:",
            "sibling_distance": 2,
        },
        {
            "string": "ANIME AIR START",
            "json": "anime_air_start",
        },
        {
            "string": "ANIME AIR END",
            "json": "anime_air_end",
        },
        {
            "string": "ANIME PREMIERED",
            "json": "anime_premiered",
            "search_key": "Premiered:",
            "sibling_distance": 3,
        },
        {
            "string": "ANIME BROADCAST",
            "json": "anime_brodcast",
            "search_key": "Broadcast:",
            "sibling_distance": 2,
        },
        {
            "string": "ANIME PRODUCERS",
            "json": "anime_producers",
            "search_key": "Producers:",
            "first_list_index": 3,
            "list_jumper": 2,
        },
        {
            "string": "ANIME LICENSORS",
            "json": "anime_licensors",
            "search_key": "Licensors:",
            "sibling_distance": 3,
        },
        {
            "string": "ANIME STUDIOS",
            "json": "anime_studios",
            "search_key": "Studios:",
            "first_list_index": 3,
            "list_jumper": 2,
        },
        {
            "string": "ANIME SOURCE",
            "json": "anime_source",
            "search_key": "Source:",
            "sibling_distance": 2,
        },
        {
            "string": "ANIME GENRES",
            "json": "anime_genres",
            "search_key": "Genres:",
            "first_list_index": 4,
            "list_jumper": 3,
        },
        {
            "string": "ANIME THEME",
            "json": "anime_theme",
            "search_key": "Themes:",
            "first_list_index": 4,
            "list_jumper": 3,
        },
        {
            "string": "ANIME DEMOGRAPHIC",
            "json": "anime_demographic",
            "sibling_distance": 3,
            "search_key": "Demographic:",
        },
        {
            "string": "ANIME DURATION",
            "json": "anime_duration",
            "sibling_distance": 2,
            "search_key": "Duration:",
        },
        {
            "string": "ANIME RATING",
            "json": "anime_rating",
            "sibling_distance": 2,
            "search_key": "Rating:",
        },
        {
            "string": "MY COMMENTS",
            "xml": "my_comments",
            "json": "my_comments",
        },
        {
            "string": "MY DISCUSS",
            "xml": "my_discuss",
            "json": "my_discuss",
        },
        {
            "string": "MY FINISH DATE",
            "xml": "my_finish_date",
            "json": "my_finish_date",
        },
        {
            "string": "MY ID",
            "xml": "my_id",
            "json": "my_id",
        },
        {
            "string": "MY PRYORITY",
            "xml": "my_priority",
            "json": "my_priority",
        },
        {
            "string": "MY RATED",
            "xml": "my_rated",
            "json": "my_rated",
        },
        {
            "string": "MY REWATCH VALUE",
            "xml": "my_rewatch_value",
            "json": "my_rewatch_value",
        },
        {
            "string": "MY REWATCHING",
            "xml": "my_rewatching",
            "json": "my_rewatching",
        },
        {
            "string": "MY REWATCHING EP",
            "xml": "my_rewatching_ep",
            "json": "my_rewatching_ep",
        },
        {
            "string": "MY SCORE",
            "xml": "my_score",
            "json": "my_score",
        },
        {
            "string": "MY SNS",
            "xml": "my_sns",
            "json": "my_sns",
        },
        {
            "string": "MY START DATE",
            "xml": "my_start_date",
            "json": "my_start_date",
        },
        {
            "string": "MY STATUS",
            "xml": "my_status",
            "json": "my_status",
        },
        {
            "string": "MY STORAGE",
            "xml": "my_storage",
            "json": "my_storage",
        },
        {
            "string": "MY STORAGE VALUE",
            "xml": "my_storage_value",
            "json": "my_storage_value",
        },
        {
            "string": "MY TAGS",
            "xml": "my_tags",
            "json": "my_tags",
        },
        {
            "string": "MY TIMES WATCHED",
            "xml": "my_times_watched",
            "json": "my_times_watched",
        },
        {
            "string": "MY WATCHED EPISODES",
            "xml": "my_watched_episodes",
            "json": "my_watched_episodes",
        },
        {
            "string": "UPDATE ON IMPORT",
            "xml": "update_on_import",
            "json": "update_on_import",
        },
    ],
}

NAME = 0
ID = 1
SCORE = 2


def escape(list, str, strip=True):
    for escape in list:
        str = str.replace(escape, "")

    if strip:
        return str.strip()
    else:
        return str


def extract(soup, attribute):
    if attribute.get("search_key") is None:
        var = attribute.get("string")
        if var == "ANIME NAME":
            return soup.find("h1", class_="title-name").contents[0].string
        elif var == "ANIME ID":
            return soup.find("input", attrs={"name": "aid"}).attrs["value"]
        elif var == "ANIME AIR START":
            return escape(
                (","),
                soup.find("span", string="Aired:")
                .parent.contents[2]
                .string.split("to")[0],
            ).strip()
        elif var == "ANIME AIR END":
            return escape(
                (","),
                soup.find("span", string="Aired:")
                .parent.contents[2]
                .string.split("to")[1],
            ).strip()
        else:
            if attribute.get("xml") is None:
                return "ERROR"
            else:
                return "USE XML"

    else:
        if attribute.get("first_list_index") is None:
            return escape(
                attribute.get("escape_list", ()),
                soup.find("span", string=attribute.get("search_key", ""))
                .parent.contents[attribute.get("sibling_distance", 0)]
                .string,
            )

        else:
            val = []
            temp = soup.find(
                "span", string=attribute.get("search_key", "")
            ).parent.contents
            for i in range(
                attribute.get("first_list_index", 0),
                len(temp),
                attribute.get("list_jumper", 1),
            ):
                val.append(temp[i].string)

            return val


def update_score(a_list, anime):
    anime_id = anime[COSTANT["anime_attributes"][ID]["xml"]]

    req = requests.get(COSTANT["web_link_start"] + anime_id, timeout=5)

    new = {}

    soup = BeautifulSoup(req.text, "html.parser")

    for attribute in COSTANT["anime_attributes"]:
        new_key = attribute.get("json", "ERROR")
        if attribute.get("xml") is None:
            new[new_key] = extract(soup, attribute)
        else:
            new[new_key] = anime.get(attribute.get("xml", "ERROR"), "ERROR")

    a_list.append(new)

    return


# get xml from file
with open(FILE_NAME, encoding="utf-8") as fd:
    doc = xmltodict.parse(fd.read())

    # print(json.dumps(doc, indent=4))

    # list of dictionary
    list_xml = doc.get("myanimelist").get("anime")

    if list_xml.__class__ is not list:
        list_xml = [list_xml]

    anime_list = []

    if USE_MULTITHREADING:
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            for anime in list_xml:
                executor.submit(update_score, anime_list, anime)

            executor.shutdown(wait=True)

    else:
        for anime in list_xml:
            update_score(anime_list, anime)

    a_dict = {}
    a_dict["list"] = anime_list

    # print(json.dumps(a_dict, indent=4))

    json_name = FILE_NAME.split(".", maxsplit=1)[0] + ".json"

    # save the list in a json file
    with open(json_name, "w", encoding="utf-8") as outfile:
        json.dump(a_dict, outfile, indent=4)
