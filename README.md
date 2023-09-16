# View MAL anime list in order of the site score

EDIT 17-09-2023: MAL does not let me anymore use this program to check all the anime's info, so for now there will be no more update.

From your anime list, just export your anime list and put it in the same folder of the repo.

- set the name of the xml file downloaded in FILE_NAME
- change your parameters
  - in gen_json_file could you choose if you want to use multythreading (suggested), the max number of threads, and a beta feature for try to not be blocked by mal
  - in read_json_file how you want to display the results, filters and order

Library used (that needs to be installed with pip: requests, xmltodict, beautifulsoup4)

# WARINGN MAL can detect the program as a bot and lock you out of the site for some times, use at your risk
