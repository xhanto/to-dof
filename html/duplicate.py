import pandas as pd
import pickle
import re
sets = ["armes","consommables","equipements","ressources"]
sets = ["familiers"]
s2 = ["Arme","Consommable","Equipement","Ressource"]
d = dict()
l = []
data = []
ind = 0
c = 0
for s in sets:
    l = []
    data=[]
    print "-----" + s + "-----"
    for i in range(9):
        df = pd.read_pickle("C:/Users/BoS/Desktop/site/html/" + s + str(i) + ".pickle")
                #d.update({ID: row.id, type: unicode(row.type)})
        for row in df:
            ind = re.findall(r'[0-9]+',row)

            if ind[0] in l:
                c = c+1
                continue

            else:
                l.append(ind[0])
                data.append(row)

    print len(l)
    pickle.dump(data,open(s+"_links.pickle", "wb"))

print c
