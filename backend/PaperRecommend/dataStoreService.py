import random
import urllib.request as libreq
from .models import Paper
import xmltodict as xmltodict
#from keybert import KeyBERT


def storeData():
    search = []
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
                newPaper.save()
                print(newPaper.area)
                print(i)

def get_keywords(doc: str):
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 3), top_n=5, use_mmr=True, diversity=0.7)
    return [keyword[0] for keyword in keywords]


def summaryGet():

    allData = Paper.objects.all()
    summary = []
    file = open('data1.txt', 'w', encoding='utf-8')
    count = 0
    for a in allData:
        summary.append(a.abstract)
        file.write(str(count)+'  '+a.abstract + '\n')
        count = count +1
    file.close()
    print(len(summary))

    return summary

''' this method is one time used and will not be used anymore
def keywordsGet():
    allData = Paper.objects.filter(keywords='')
    print(len(allData))
    for d in allData:
        keywordsStr = ''
        keywords = get_keywords(d.abstract)
        for words in keywords:
            if words == '':
                keywordsStr = str(words)
            else:
                keywordsStr = keywordsStr+','+str(words)
        d.keywords = keywordsStr
        d.save()
        print(keywordsStr)'''




def getDataByArea(area):
    return Paper.objects.filter(area = area)


def randomKeywords(area):
    areaData = Paper.objects.filter(area='stat.ME')
    a = []
    print(len(areaData))
    for i in range (0, 10, 1):
        a.append(random.randint(0,len(areaData)))
    for number in a:
        print(areaData[number])






