# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20160627_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='server',
            field=models.IntegerField(choices=[(0, b'Non sp\xc3\xa9cifi\xc3\xa9'), (1, b'Padgref'), (2, b'Helioboros'), (3, b'Aermyne'), (4, b'Shika'), (5, b'Ombre'), (6, b'Ereziah'), (7, b'Bolgrot'), (8, b'Rosal'), (9, b'Nehra'), (10, b'Aguabrial'), (11, b'Dark Vlad'), (12, b'Solar'), (13, b'Edasse'), (14, b'Spiritia'), (15, b'Zato\xc3\xafshwan'), (16, b'T\xc3\xa9n\xc3\xa8bre'), (17, b'Buhorado'), (18, b'Nomekop'), (19, b'Alma'), (20, b'Danathor'), (21, b'Maimane'), (22, b'Oto Mustam'), (23, b'Rushu'), (24, b'Lily'), (25, b'Silouate'), (26, b'Li Crounch'), (27, b'Hecate'), (28, b'Kuri'), (29, b'Allister'), (30, b'Farle'), (31, b'Raval'), (32, b'Jiva'), (33, b'Menalt'), (34, b'Bowisse'), (35, b'Domen'), (36, b'Sumens'), (37, b'Hyrkul'), (38, b'Vil Smisse'), (39, b'Amayiro'), (40, b'Pouchecot'), (41, b'Otoma\xc3\xaf'), (42, b'Rykke-Errel'), (43, b'Helsephine'), (44, b'Silvosse'), (45, b'Djaul'), (46, b'Crocoburio'), (47, b'Goultard'), (48, b'Brumaire'), (49, b'Ulette'), (50, b'Mylaise'), (51, b'Many'), (52, b'Hel Munster'), (53, b'Agride')], default=0),
        ),
    ]
