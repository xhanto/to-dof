import pandas as pd

sets = ["armes","consommables","equipements","ressources"]
s2 = ["Arme","Consommable","Equipement","Ressource"]
d = dict()
l = []
data = []
ind = 0
for s in sets:
    print "--- Processing " + s + " ---"
    for i in range(21):
        print "------ Pickle " + str(i+1)
        df = pd.read_pickle("C:/Users/BoS/Desktop/site/html/" + s + "_data" + str(i+1) + ".pickle")
        for row in df.itertuples():
                #d.update({ID: row.id, type: unicode(row.type)})
            if row.id in l:
                continue
            else:
                l.append(row.id)
                entry = dict(
                    id = row.id,
                    table = s2[ind]
                )
                data.append(entry)
    ind = ind+1
df_out = pd.DataFrame(data)
df_out.to_pickle("ids.pickle")
print df_out
