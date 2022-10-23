import urllib.request as libreq

#with libreq.urlopen('http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1') as url:
 #   r = url.read()


with libreq.urlopen('http://export.arxiv.org/api/query?search_query=start=0&max_results=1') as url:
    r = url.read()
    r = r.decode('utf8').replace("'", '"')

print(type(r))
print(r)