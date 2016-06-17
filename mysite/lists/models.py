from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import json

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    list_count = models.IntegerField(default=0)
    server = models.CharField(max_length=60,blank=True,null=True)
    mp = models.CharField(max_length=100,blank=True,null=True)

    def __unicode__(self):
        return self.user.username

class List(models.Model):
    list_name = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    server = models.CharField(max_length=60,blank=True,null=True)
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
    table = models.CharField(max_length=20)
    list_display = ('ID')
    def __unicode__(self):
        return str(self.ID)

class ListItem(models.Model):
    ID = models.ForeignKey(List)
    itemID = models.ForeignKey(Objet)
    list_display = ('ID')
    def __unicode__(self):
            return str(self.ID)

class Ressource(models.Model):
    ID = models.ForeignKey(Objet,default=0)
    name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(default=0)
    type = models.CharField(max_length=50)
    effects = models.TextField()
    caracs = models.TextField()
    conds = models.TextField()
    recipe = models.TextField()
    list_display = ('ID')
    def __unicode__(self):
        return str(self.ID)
    def seteffects(self,x):
        self.effects = json.dumps(x)
    def geteffects(self,x):
        return json.loads(self.effects)

    def setcaracs(self,x):
        self.caracs = json.dumps(x)
    def getcaracs(self,x):
        return json.loads(self.caracs)

    def setconds(self,x):
        self.conds = json.dumps(x)
    def getconds(self,x):
        return json.loads(self.conds)

    def setrecipe(self,x):
        self.recipe = json.dumps(x)
    def getrecipe(self,x):
        return json.loads(self.recipe)

class Arme(models.Model):
    ID = models.ForeignKey(Objet,default=0)
    name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(default=0)
    type = models.CharField(max_length=50)
    effects = models.TextField()
    caracs = models.TextField()
    conds = models.TextField()
    recipe = models.TextField()
    list_display = ('ID')

    def __unicode__(self):
        return str(self.ID)

    def seteffects(self,x):
        self.effects = json.dumps(x)
    def geteffects(self,x):
        return json.loads(self.effects)

    def setcaracs(self,x):
        self.caracs = json.dumps(x)
    def getcaracs(self,x):
        return json.loads(self.caracs)

    def setconds(self,x):
        self.conds = json.dumps(x)
    def getconds(self,x):
        return json.loads(self.conds)

    def setrecipe(self,x):
        self.recipe = json.dumps(x)
    def getrecipe(self,x):
        return json.loads(self.recipe)

class Equipement(models.Model):
    ID = models.ForeignKey(Objet,default=0)
    name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(default=0)
    type = models.CharField(max_length=50)
    effects = models.TextField()
    caracs = models.TextField()
    conds = models.TextField()
    recipe = models.TextField()
    list_display = ('ID')

    def __unicode__(self):
        return str(self.ID)

    def seteffects(self,x):
        self.effects = json.dumps(x)
    def geteffects(self,x):
        return json.loads(self.effects)

    def setcaracs(self,x):
        self.caracs = json.dumps(x)
    def getcaracs(self,x):
        return json.loads(self.caracs)

    def setconds(self,x):
        self.conds = json.dumps(x)
    def getconds(self,x):
        return json.loads(self.conds)

    def setrecipe(self,x):
        self.recipe = json.dumps(x)
    def getrecipe(self,x):
        return json.loads(self.recipe)

class Consommable(models.Model):
    ID = models.ForeignKey(Objet,default=0)
    name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(default=0)
    type = models.CharField(max_length=50)
    effects = models.TextField()
    caracs = models.TextField()
    conds = models.TextField()
    recipe = models.TextField()
    list_display = ('ID')

    def __unicode__(self):
        return str(self.ID)

    def seteffects(self,x):
        self.effects = json.dumps(x)
    def geteffects(self,x):
        return json.loads(self.effects)

    def setcaracs(self,x):
        self.caracs = json.dumps(x)
    def getcaracs(self,x):
        return json.loads(self.caracs)

    def setconds(self,x):
        self.conds = json.dumps(x)
    def getconds(self,x):
        return json.loads(self.conds)

    def setrecipe(self,x):
        self.recipe = json.dumps(x)
    def getrecipe(self,x):
        return json.loads(self.recipe)
