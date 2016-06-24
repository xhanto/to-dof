import pandas as pd

sets = ["armes","consommables","equipements","ressources"]
s2 = ["Arme","Consommable","Equipement","Ressource"]
d = dict()
l = []
data = []
ind = 0
c = 0
for s in sets:
    print "--- Processing " + s + " ---"
    for i in range(21):
        print "------ Pickle " + str(i+1)
        df = pd.read_pickle("C:/Users/BoS/Desktop/site/html/" + s + "_data" + str(i+1) + ".pickle")
        for row in df.itertuples():
                #d.update({ID: row.id, type: unicode(row.type)})

            if row.id in l:
                c = c+1
                print row.name
                continue
            else:
                l.append(row.id)
                j = row.name.replace(u"\u0152",'Oe')
                if row.name == "Aigu":
                    j = "Aigue-Marine"
                elif row.name == "Pierre d'Aigu":
                    j = "Pierre d'Aigue-Marine"
                entry = dict(
                    id = row.id,
                    name = unicode(j)
                )
                data.append(entry)
    ind = ind+1
df_out = pd.DataFrame(data)
df_out.to_pickle("idname.pickle")
print c
