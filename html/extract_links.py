import requests
import pickle
from math import ceil
from BeautifulSoup import BeautifulSoup

#pages = ["equipements","consommables","idoles","armes"]
pages = ["ressources"]
def count_pages(page):
    url = 'http://www.dofus.com/fr/mmorpg/encyclopedie/' + page
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    n_items = soup.find("div", { "class" : "ak-list-info" })
    return int(ceil(float(n_items.find("strong").text)/96))


def get_page(url):
    r = requests.get(url)
    while(r.status_code != requests.codes.ok):
        r = requests.get(url)
    soup = BeautifulSoup(r.content)
    return soup

def extract_links(url):
    soup = get_page(url)
    linkers = soup.findAll("span",{"class" : "ak-linker"})
    linkers= linkers[::2]
    links = []
    for l in linkers:
        a=l.findAll("a")
        for ref in a:
            links.append(ref.get("href"))
    return links


for p in pages:
    links = []
    n_pages = count_pages(p)

    for i in range(n_pages):
        url = 'http://www.dofus.com/fr/mmorpg/encyclopedie/'+p+'?size=96&page=%d' % (i+1)
        ret = extract_links(url)
        links.extend(ret)
    print len(links)
    pickle.dump(links,open(p+".pickle", "wb"))
