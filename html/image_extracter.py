# -*- coding: utf-8 -*-

import pickle
import requests
import re
import pandas as pd
import argparse
import gc
from BeautifulSoup import BeautifulSoup
import urllib

files = ['equipements','armes','consommables']
base = "http://www.dofus.com"

for f in files:

    itemlist = pickle.load(open(f+"_links.pickle","rb"))
    print "----- Obtaining " + f + " -----"
    count = len(itemlist)
    i = 0
    j = 0




    data = []
    for item in itemlist:
        #progression
        print item.encode("utf-8")
        i=i+1

        try:
            r = requests.get(base+item)
        except:
            r = requests.get(base+item)
        while(r.status_code != requests.codes.ok):
            r = requests.get(base+item)
        soup = BeautifulSoup(r.content)
        block = soup.find("img",{"class" : "img-maxresponsive"})
        url = block['src']
        m = re.search(r"(\d+)",item)
        ID = m.group(0)
        urllib.urlretrieve(url, "images/"+ID + ".jpg")
        if i%(count/20) == 0:
            j = j+1
            print "%d" % (j*5) + "%"

    print "----- " + f + " done -----"
