import requests
import xmltodict
import json
import concurrent.futures
from bs4 import BeautifulSoup



# PARAMETERS
USE_MULTITHREADING = True
MAX_WORKERS = 5

FILE_NAME = ''





# CONSTANTS (DO NOT CHANGE)
WEB_LINK_START = 'https://myanimelist.net/anime/'
ANIME_ID_STRING = 'series_animedb_id'
SITE_SCORE_LABEL = 'score-label'
SCORE_LABEL = 'score'

def update_score(a_list, number, anime_id_string, site_score_label, score_label):

    r = requests.get(WEB_LINK_START + a_list[number][anime_id_string])

    soup = BeautifulSoup(r.text, 'html.parser')

    s = soup.find('div', class_= site_score_label)
    if s is None:
        content = 'N/A'
    else:
        content = s.contents[0]

    a_list[number][score_label] = content

    return




# get xml from file
with open(FILE_NAME) as fd:
    doc = xmltodict.parse(fd.read())

    # print(json.dumps(doc, indent=4, sort_keys=True))

    # list of dictionary
    anime_list = doc['myanimelist']['anime']

    if USE_MULTITHREADING:
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            for i in range(len(anime_list)):
                executor.submit(update_score, anime_list, i, ANIME_ID_STRING, SITE_SCORE_LABEL, SCORE_LABEL)
            
            executor.shutdown(wait=True)
            
    else:
        for i in range(len(anime_list)):
            update_score(anime_list, i, ANIME_ID_STRING, SITE_SCORE_LABEL, SCORE_LABEL)
    
    new_list = sorted(anime_list, key=lambda k: k[SCORE_LABEL], reverse=True)


    json_name = FILE_NAME.split('.', maxsplit=1)[0] + '.json'

    #save the list in a json file
    with open(json_name, 'w') as outfile:
        json.dump(new_list, outfile, indent=4, sort_keys=True)



