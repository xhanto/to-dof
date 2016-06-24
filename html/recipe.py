# -*- coding: utf-8 -*-

import pandas as pd
import re

sets = ["equipements","ressources","armes"]


def split_recipe(l,base):
    data = []
    for i in l:
        i = i.replace(u"\u0152",'Oe')
        match = re.match(r"([0-9]+)(.+)", i)
        if match:
            items = match.groups()
            print base
            row = namesids.loc[namesids['name'] == items[1]]
            ind = row.iloc[0]['id']
            entry = dict(
                base_id = base,
                ing_id = ind,
                count = int(items[0])
            )
            data.append(entry)
    return data

ret = []
namesids = pd.read_pickle("C:/Users/BoS/Desktop/site/html/idname.pickle")
for s in sets:
    print "--- Processing " + s + " ---"
    for i in range(21):
        print "------ Pickle " + str(i+1)
        df = pd.read_pickle("C:/Users/BoS/Desktop/site/html/" + s + "_data" + str(i+1) + ".pickle")
        for row in df.itertuples():
            if row.recipe is not None:
                ret.extend(split_recipe(row.recipe,row.id))
df_out = pd.DataFrame(ret)
df_out.to_pickle("recipe.pickle")
print df_out
