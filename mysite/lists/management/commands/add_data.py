from django.core.management.base import BaseCommand, CommandError
from lists.models import Objet, Recette
import pandas as pd
import json

class Command(BaseCommand):
    help = 'Populate database'

    def handle(self, *args, **options):
        #
        # sets = ["armes","consommables","equipements","ressources","familiers"]
        # for s in sets:
        #     print "--- Processing " + s + " ---"
        #     for i in range(21):
        #         print "------ Pickle " + str(i+1)
        #         df = pd.read_pickle("C:/Users/BoS/Desktop/site/html/" + s + "_data" + str(i+1) + ".pickle")
        #         for row in df.itertuples():
        #
        #             item = Objet()
        #             item.ID = row.id
        #             item.recipe = json.dumps(row.recipe)
        #             item.level = row.level
        #             item.effects = json.dumps(row.effets)
        #             item.conds = json.dumps(row.conditions)
        #             item.type = unicode(row.type)
        #             item.name = unicode(row.name)
        #             item.caracs = json.dumps(row.caracs)
        #             item.save()
        df = pd.read_pickle("C:/Users/BoS/Desktop/site/html/recipe.pickle")

        for row in df.itertuples():
            recette = Recette()
            recette.item_ID_id = row.base_id
            recette.count = row.count
            recette.ing_ID_id = row.ing_id
            recette.save()
