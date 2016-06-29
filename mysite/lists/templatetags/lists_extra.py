# -*- coding: utf-8 -*-
from django import template
from lists.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
import ast
import re
from django.utils.encoding import smart_unicode
import json
from collections import Counter

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

    items_list = Objet.objects.filter(type__exact=type).filter(level__range=(ran[0],ran[1])).order_by('level')

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
def add_button(context,user,item):
    if user.is_authenticated():
        myList = List.objects.filter(user__exact=user,pub_date__lte=timezone.now()).order_by('-pub_date')

        return {'myLists': myList,'user':user, 'item': item}

@register.inclusion_tag('includes/list_view.html',takes_context=True)
def list_view(context,user,list_id, edit_form):
    liste = List.objects.filter(id__exact = list_id)
    path = "http://127.0.0.1:8000" + context['request'].get_full_path()
    items = ListItem.objects.filter(ID_id = list_id)
    if user.is_authenticated():
        return {'myList': liste[0],'items':items,'user':user,'path':path,'edit_form':edit_form}
    else:
        return {'myList':liste[0],'items':items,'path':path}

@register.filter(name='get_item')
def get_item(value):
    items = []
    for i in value:
        item = Objet.objects.filter(ID__exact=i.itemID_id)
        items.append(item[0])

    return items

@register.filter(name='get_recipe')
def get_recipe(value):

    itemID = value.ID
    recipe = Recette.objects.filter(item_ID=itemID)
    return recipe

@register.filter(name='get_range')
def get_range(value):
    return range(value+1)

@register.filter(name='verified')
def verified(user,liste):
    if user is not None:
        if user.is_authenticated() and user == liste.user:
            return True
    return False

@register.filter(name='get_total')
def get_total(values):
    counter = Counter()
    for i in values:
        recipe = Recette.objects.filter(item_ID=i.itemID_id)
        for r in recipe:
            counter.update({r.ing_ID:r.count})

    items = []
    for k in counter.keys():
        items.append({'item': k,'count':counter[k]})
    return items
