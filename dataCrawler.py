import ast
import json
import urllib.request as libreq

#with libreq.urlopen('http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1') as url:
 #   r = url.read()
import requests
import xmltodict as xmltodict

with libreq.urlopen('http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1') as url:

    r = url.read()
    r = r.decode('utf8').replace("'", '"')
    print(r)
    r = xmltodict.parse(r)
    print(r)
    print(r['opensearch:itemsPerPage']['title'])
    #data = ast.literal_eval(r)
    #json_file = json.load(url.read())







