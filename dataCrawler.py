import urllib.request as libreq

import xmltodict as xmltodict

with libreq.urlopen('http://export.arxiv.org/api/query?search_query=all:math.GN&start=5&max_results=10') as url:
    r = url.read()
    r = r.decode('utf8').replace("'", '"')
  #  print(r)
    r = xmltodict.parse(r)
  #  print(r['feed'])
    '''
    print(r['feed'])
    print(r['feed']['entry'][0])
    print(r['feed']['entry'][1])
    print(r['feed']['entry'][2])
    print(r['feed']['entry'][3])
    print(r['feed']['entry'][4])'''
    for i in range(0, 5, 1):
        print(r['feed']['entry'][i])
        currentPaper = r['feed']['entry'][i]
        title = currentPaper['title'].replace('\n', '')
        print('title :' + title)
        print('author name :' +str( currentPaper['author']))
        if 'name' in currentPaper['author']:
            print(currentPaper['author']['name'])
            print(1)
        else:
            print(2)
            print(currentPaper['author'][0]['name'])


        #author = currentPaper['author'][0]['name']
        abstract = currentPaper['summary'].replace('\n', '')
        print('abstract : ' + abstract)
        print('published time :' + currentPaper['published'])
        link = currentPaper['id']
        print('link: ' + link)
        # print('comment: '+str(currentPaper['arxiv:comment']))
        if 'arxiv:comment' in currentPaper:
            print('comment: ' + str(currentPaper['arxiv:comment']['#text']))
            comment = str(currentPaper['arxiv:comment']['#text']).replace('\n', '')

    #  print(r['feed']['entry']['title'])
    #  print(r['feed']['entry']['summary'])
    # DOMTree = xml.dom.minidom.parse(r)
    '''r = xmltodict.parse(r)
    print(r)
    print(r['opensearch:itemsPerPage']['title'])
    #data = ast.literal_eval(r)
    #json_file = json.load(url.read())
    DOMTree = xml.dom.minidom.parse(r)'''
#  print(type(DOMTree))
