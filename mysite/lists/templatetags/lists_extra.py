# -*- coding: utf-8 -*-
from django import template
from lists.models import List,UserProfile,User,Ressource,Arme,Equipement
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
import ast
import re
from django.utils.encoding import smart_unicode
import json


register = template.Library()

@register.inclusion_tag('includes/side_menu.html',takes_context=True)
def sidebar(context,user):
    if user.is_authenticated():
        serv = UserProfile.objects.filter(user__exact=user)
        serverList = []
        myList = List.objects.filter(user__exact=user,pub_date__lte=timezone.now()).order_by('-pub_date')
        if serv:
            serverList = List.objects.filter(server__exact=serv[0].server).order_by('-pub_date')

        return {'myLists': myList,'serverList':serverList,'user':user}


@register.inclusion_tag('includes/item_list.html',takes_context=True)
def itemlist(context,type,ran,p,user,request):
    armes = ['Hache','Bâton','Arc','Épée','Dague','Baguette','Pelle','Marteau']
    equipements = ['Bouclier','Anneau','Amulette','Cape','Bottes','Chapeau','Ceinture','Trophée','Sac à dos']
    ressources = ['Idole']

    if type in armes:
        items_list = Arme.objects.filter(type__exact=type).filter(level__range=(ran[0],ran[1])).order_by('level')
    elif type in equipements:
        items_list = Equipement.objects.filter(type__exact=type).filter(level__range=(ran[0],ran[1])).order_by('level')
    elif type in ressources:
        items_list = Ressource.objects.filter(type__exact=type).filter(level__range=(ran[0],ran[1])).order_by('level')
        return 0
    paginator = Paginator(items_list,50)
    page = request.GET.get('page')

    if "newlist" in str(context):
        if context["newlist"]:
            page = p
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)

    return {'list': items,'type': type, 'ran': ran,'user': user}
@register.filter(name='parse')
def parse(value,type):
    jsonDec = json.decoder.JSONDecoder()
    l = jsonDec.decode(value)
    ret = []
    if type == "recipe":
        for i in range(len(l)):
            if i == len(l)-1:
                ret.append(re.sub(r'^([0-9]+)',r'\1x ',l[i]))
            else:
                ret.append(re.sub(r'^([0-9]+)',r'\1x ',l[i])+", ")
        return ret
    elif type =="caracs":
        for i in l:
            for j in range(len(i))[::2]:
                ret.append(i[j]+": "+i[j+1])
        return ret
    elif type == "conds":
        tmp=[]
        for i in l:
            for j in i:
                tmp.append(j.split("ou"))
        for i in tmp:
            for j in i:
                ret.append(j)
        return ret
    else:
        return l
@register.filter(name='render')
def render(value):
    if value =="Sac à dos":
        return "Sac"
    elif value == "Bâton":
        return "Baton"
    elif value == "Trophée":
        return "Trophee"
    elif value == "Épée":
        return "Epee"
    else:
        return value

@register.filter(name='title')
def title(value):
    s = ['Idole','Hache','Bâton','Arc','Épée','Dague','Baguette','Pelle','Ceinture','Trophée','Bouclier','Amulette','Cape']
    x = ['Marteau','Anneau','Chapeau']


    if value =="Sac à dos":
        return "Sacs à dos"
    elif value == "Bottes":
        return value
    elif value in s:
        return value+"s"
    elif value in x:
        return value+"x"
    else:
        return value

@register.filter(name='get_mp')
def get_mp(value):
    profile = UserProfile.objects.filter(user__exact=value)
    return profile[0].mp


@register.inclusion_tag('includes/add_button.html',takes_context=True)
def add_button(context,user):
    if user.is_authenticated():
        myList = List.objects.filter(user__exact=user,pub_date__lte=timezone.now()).order_by('-pub_date')
        return {'myLists': myList,'user':user}
