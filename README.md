# View MAL anime list in order of the site score

From your anime list, just export your anime list and put it in the same folder of the two python file.

- ordered_by_site_score.py: will connect to the internet for collect all the score for each anime in your list (if the anime is Not Yet Aired his score will be N/A), and save them in a json File. You just have to set the file name and if you want to use multithreading (i suggest so, if you have a lot of anime doing it sequentially could take some times).
- json_anime_reader.py: will print the list from the json file using the parameter setted, like before add the name file and set yotu settings.

Library used (that needs to be installed with pip: requests, xmltodict, beautifulsoup4)
