import json

ONLY_PLAN_TO_WATCH = True
ASCENDING = False
MIN_SCORE = 7.5
ACTIVATE_LINK = True
FILE_NAME = 'animelist_1694175851_-_16749231.json'



SCORE_LABEL = 'score'
STATUS_LABEL = 'my_status'
PLAN_TO_WATCH_LABEL = 'Plan to Watch'
TITLE_LABEL = 'series_title'
ANIME_ID_LABEL = 'series_animedb_id'
WEB_LINK_START = 'https://myanimelist.net/anime/'


# get json from file
with open(FILE_NAME) as fd:

    # list of dictionary
    anime_list = json.load(fd)

    # print(json.dumps(anime_list, indent=4, sort_keys=True))

    # sort by score
    anime_list = sorted(anime_list, key=lambda k: k[SCORE_LABEL], reverse=True)

    # print(json.dumps(new_list, indent=4, sort_keys=True))

    # print anime name and score
    for anime in reversed(anime_list) if ASCENDING else anime_list:
        if ONLY_PLAN_TO_WATCH and anime[STATUS_LABEL] != PLAN_TO_WATCH_LABEL:
            continue

        if anime[SCORE_LABEL] == 'N/A':
            continue

        if float(anime[SCORE_LABEL]) < MIN_SCORE:
            continue

        print(anime[SCORE_LABEL] + ' - ' + anime[TITLE_LABEL] + (' - ' + WEB_LINK_START + anime[ANIME_ID_LABEL] if ACTIVATE_LINK else ''))