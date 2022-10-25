import urllib.request as libreq
from .models import Paper
import xmltodict as xmltodict


def storeData():
    with libreq.urlopen('http://export.arxiv.org/api/query?search_query=all:electron&start=273&max_results=227') as url:
        r = url.read()
        r = r.decode('utf8').replace("'", '"')
        #print(r)
        r = xmltodict.parse(r)
        #print(r['feed'])

        for i in range(0, 299, 1):
            #   print(r['feed']['entry'][i])
            currentPaper = r['feed']['entry'][i]
            title = currentPaper['title'].replace('\n', '')
            #  print('title :' + title)
            #   print('author name :' + currentPaper['author'][0]['name'])
            if 'name' in currentPaper['author']:
                author = currentPaper['author']['name']
            else:
                author = currentPaper['author'][0]['name']
            abstract = currentPaper['summary'].replace('\n', '')
            #  print('abstract : ' + abstract)
            #  print('published time :' + currentPaper['published'])
            time = currentPaper['published']
            link = currentPaper['id']
            #  print('link: ' + link)
            #  print('comment: '+str(currentPaper['arxiv:comment']['#text']))
            area = 'electron'
            newPaper = Paper(area=area, title=title, author=author, abstract=abstract, link=link, publishTime=time)
            if 'arxiv:comment' in currentPaper:
                comment = currentPaper['arxiv:comment']['#text'].replace('\n', '')
                newPaper.comment = comment
            #      print('comment: ' + str(currentPaper['arxiv:comment']['#text']))
            newPaper.save()
            print(newPaper)
            print(i)
