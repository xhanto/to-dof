from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from lists.choices import *
import json

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    list_count = models.IntegerField(default=0)
    server = models.IntegerField(choices=SERVER_CHOICES, default=0)
    mp = models.CharField(max_length=100,blank=True,null=True)

    def __unicode__(self):
        return self.user.username

class List(models.Model):
    list_name = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    server = models.IntegerField(choices=SERVER_CHOICES, default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=True)
    list_display = ('list_name', 'user')
    def __unicode__(self):
        return self.list_name
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Objet(models.Model):
    ID = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100,db_index=True)
    level = models.PositiveSmallIntegerField(default=0)
    type = models.CharField(max_length=50)
    effects = models.TextField()
    caracs = models.TextField()
    conds = models.TextField()
    recipe = models.TextField()
    list_display = ('ID')
    def __unicode__(self):
        return str(self.ID)

class ListItem(models.Model):
    ID = models.ForeignKey(List)
    itemID = models.ForeignKey(Objet)
    count = models.PositiveSmallIntegerField(default = 0)
    priority = models.PositiveSmallIntegerField(default = 0)
    value = models.PositiveIntegerField(default = 0)
    list_display = ('ID')
    def __unicode__(self):
            return str(self.ID)

class Recette(models.Model):
    item_ID =  models.ForeignKey('Objet',related_name="item_ID")
    ing_ID =  models.ForeignKey('Objet',related_name="ing_ID")
    count = models.PositiveSmallIntegerField(default=0)
    list_display = ('item_ID')
    def __unicode__(self):
        return str(self.item_ID)
