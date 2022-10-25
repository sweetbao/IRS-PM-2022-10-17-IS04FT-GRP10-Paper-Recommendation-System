import urllib.request as libreq
from .models import Paper
import xmltodict as xmltodict


def storeData():
    search = ['q-bio.TO','q-fin.CP','q-fin.EC','q-fin.GN','q-fin.MF','q-fin.PM','q-fin.PR','q-fin.RM','q-fin.ST','q-fin.TR','stat.AP','stat.CO','stat.ME','stat.ML','stat.OT','stat.TH']
    for tag in search:
        l = 'http://export.arxiv.org/api/query?search_query=all:'+tag+'&start=0&max_results=500'
        with libreq.urlopen(l) as url:
            r = url.read()
            r = r.decode('utf8').replace("'", '"')
            # print(r)
            r = xmltodict.parse(r)
            # print(r['feed'])

            for i in range(0, 500, 1):
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
                area = tag
                newPaper = Paper(area=area, title=title, author=author, abstract=abstract, link=link, publishTime=time)
                if 'arxiv:comment' in currentPaper:
                    comment = currentPaper['arxiv:comment']['#text'].replace('\n', '')
                    newPaper.comment = comment
                #      print('comment: ' + str(currentPaper['arxiv:comment']['#text']))
               # newPaper.save()
                print(newPaper.area)
                print(i)


