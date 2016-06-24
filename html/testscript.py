# -*- coding: utf-8 -*-

import pandas as pd


df = pd.read_pickle("C:/Users/BoS/Desktop/site/html/ressources_data21.pickle")
# l = []
# for i in df.iterrows():
#
#     if "Jus" in i[1]['name']:
#         j = i[1]['name'].replace(u"\u0153",'Oe')
#         print i
data = []
entry = dict(
        id = 17853,
        name = unicode("Jus de poisson méphitique","utf-8"),
        type = unicode("Jus de poisson","utf-8"),
        level = 200,
        effets = [],
        caracs = [],
        conditions = [],
        recipe = []
        )
data.append(entry)
df2 = pd.DataFrame(data)
df3 = df.append(df2)
df3.to_pickle("ressources_data21.pickle")
