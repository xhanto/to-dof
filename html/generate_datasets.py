# -*- coding: utf-8 -*-

import pickle
import requests
import re
import pandas as pd
import argparse
import gc
from BeautifulSoup import BeautifulSoup


def get_type_level(soup):
    block = soup.find("div",{"class" : "ak-encyclo-block-info "})
    tp = unicode(block.find("span").string)
    lvl = block.find("div",{"class" : "ak-encyclo-detail-level col-xs-6 text-right"}).string
    m = re.search(r"(\d+)",lvl)
    lvl = m.group(0)
    return [tp,lvl]

def get_stats(soup):
    blocks = soup.findAll("div",{"class" : "ak-container ak-content-list ak-displaymode-col"})
    panel_titles = soup.findAll("div",{"class":"ak-panel-title"})
    effets = []
    caracs = []
    conds = []
    panel_titles = [unicode(x.text) for x in panel_titles]
    for i in range(len(blocks)):
            titles = blocks[i].findAll("div",{"class":"ak-title"})
            for t in titles:
                if "Effets" in panel_titles and i == 0:
                    effets.append(unicode(t.string.strip()))
                elif i > 0 and unicode("Caractéristiques","utf-8") in panel_titles and "Conditions" in panel_titles:
                    if i == 1:
                        sp = t.text.split(':')
                        caracs.append([unicode(x) for x in sp])
                    else:
                        sp = t.text.split('et')
                        conds.append([unicode(x) for x in sp])
                elif i > 0 and unicode("Caractéristiques","utf-8") in panel_titles and not "Conditions" in panel_titles:
                    sp = t.text.split(':')
                    caracs.append([unicode(x) for x in sp])
                elif i > 0 and not unicode("Caractéristiques","utf-8") in panel_titles and "Conditions" in panel_titles and i > 0:
                    sp = t.text.split('et')
                    conds.append([unicode(x) for x in sp])

    return [effets,caracs,conds]

def get_recipe(soup):

    crafts=soup.find("div",{"class" : "ak-container ak-panel ak-crafts"})
    recette=[]
    if crafts is not None:
        times = crafts.findAll("div",{"class" : "ak-front"})
        names = crafts.findAll("span",{"class":"ak-linker"})
        names = names[1::2]

        for k in range(len(names)):
            t = times[k].string
            m = re.search(r"(\d+)",t)
            t = m.group(0)
            recette.append(t+unicode(names[k].string))
    return recette

def recover(filename):
    df_rec = pd.read_pickle(filename + "_data2.pickle")
    return len(df_rec)

files = ["ressources","equipements","consommables"]
base = "http://www.dofus.com"

parser = argparse.ArgumentParser(description='Dataset generation')
parser.add_argument('recovery',type=bool,nargs='?',help="Recovery mode (True / False)",default=False)
try:
    args = parser.parse_args()
except:
    parser.print_help()
    parser.exit(0)

recovery = args.recovery

for f in files:

    itemlist = pickle.load(open(f+".pickle","rb"))
    print "----- Obtaining " + f + " -----"
    count = len(itemlist)
    i = 0
    j = 0
    if recovery:
        start = recover(f)
    else:
         start = 0

    data = []
    for item in itemlist:
        #progression
        print item.encode("utf-8")
        i=i+1
        if i < start+1:
            if i%(count/10) == 0:
                j = j+1
            continue
        try:
            r = requests.get(base+item)
        except:
            r = requests.get(base+item)
        while(r.status_code != requests.codes.ok):
            r = requests.get(base+item)
        soup = BeautifulSoup(r.content)

        # Get type & level

        typelvl = get_type_level(soup)

        #if(typelvl[0] not in conso):

        #    break
        # Get name
        head = soup.find("head")
        title = head.find("title").string
        name = title.split("-")[0][:-1]

        # Get ID
        m = re.search(r"(\d+)",item)
        ID = m.group(0)

        # Get stats
        stats = get_stats(soup)

        # Get craft
        craft = get_recipe(soup)

        # Get rekt
        entry = dict(
            id = ID,
            name = name,
            type = typelvl[0],
            level = typelvl[1],
            effets = stats[0],
            caracs = stats[1],
            conditions = stats[2],
            recipe = craft
        )

        data.append(entry)

        if i%(count/20) == 0:
            j = j+1
            print "%d" % (j*5) + "%"
            dft = pd.DataFrame(data)
            if recovery:
                dft.to_pickle(f+"_data_rec" + str(j) + ".pickle")
            else:
                dft.to_pickle(f+"_data" + str(j) + ".pickle")
            data = []
            del dft
            gc.collect()

    if recovery:
        df_rec = pd.DataFrame(data)
        df_rec.to_pickle(f+"_data_rec.pickle")

    else:
        df = pd.DataFrame(data)
        df.to_pickle(f+"_data.pickle")
    print "----- " + f + " done -----"
