import sys,os
sys.path.append("C:\Users\BoS\Desktop\site\mysite/")
from lists.models import Arme,Ressource,Consommable,Equipement
import pandas as pd
sets = ["armes","consommables","equipements","ressources"]
for s in sets:
    if sets == "armes" or sets == "ressources":
        r = 21
    else:
        r = 11
    for i in range(r):
        df = pd.read_pickle("C:/Users/BoS/Desktop/site/html/" + s + "_data" + str(i+1) + ".pickle")

        break
    break
