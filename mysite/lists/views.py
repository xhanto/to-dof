# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404,render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from .models import User,List,UserProfile, ListItem, Objet
from .forms import UserForm, UserProfileForm, NewListForm
from django.template import RequestContext

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request,'lists/index.html',context)
#
# def detail(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,'lists/detail.html',{'question':question})
# def results(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,'lists/results.html',{'question':question})

class IndexView(generic.ListView):
    template_name = 'lists/index.html'
    context_object_name = 'lists'

    def get_queryset(self):
        return List.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

class DetailView(generic.DetailView):
    model = List
    template_name = 'lists/detail.html'

def register(request):

    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'lists/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)


def user_login(request):
    context = RequestContext(request)
    error = False
    active = True
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/lists/')
            else:
                active = False
        else:
            print "Mauvais nom d'utilisateur ou mot de passe: {0}, {1}".format(username, password)
            error = True

    return render(request,'lists/login.html', {'error': error, 'active':active}, context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/lists/')

@login_required
def create_list(request):
    context = RequestContext(request)
    completed=False
    if request.method == 'POST':
        list_form = NewListForm(data=request.POST)
        if list_form.is_valid():
            newlist = list_form.save(commit=False)
            newlist.user = request.user
            serv = UserProfile.objects.filter(user__exact=request.user)
            print serv
            if serv:
                newlist.server = serv[0].server
            newlist.save()
            completed=True
        else:
            print list_form.errors
    else:
        list_form = NewListForm()
    dict_ret = {'newlist': True, 'list_form': list_form,'completed':completed}
    url =  request.META['HTTP_REFERER']
    p = url.split("lists")

    if "details" in p[1]:
        p = p[1].split("/")
        if "page" in p[4]:
            n = p[4].split('=')[1]
        else:
            n = 1
        add_dict = {'type': p[2], 'ran': [p[3],p[4].split("?")[0]],'page': n}
        dict_ret.update(add_dict)
    return render(request,'lists/index.html',dict_ret,context)

@login_required
def create_and_add(request,item_id):
    context = RequestContext(request)
    completed=False
    added = False
    if request.method == 'POST':
        list_form = NewListForm(data=request.POST)
        if list_form.is_valid():
            newlist = list_form.save(commit=False)
            newlist.user = request.user
            serv = UserProfile.objects.filter(user__exact=request.user)
            if serv:
                newlist.server = serv[0].server
            newl = newlist.save()
            item_list = ListItem()
            item_list.itemID = item_id
            item_list.ID = newl.id
            item_list.save()
            completed=True
            added = True
        else:
            print list_form.errors
    else:
        list_form = NewListForm()
    dict_ret = {'newlist': True, 'list_form': list_form,'completed':completed,'added':added}

    url =  request.META['HTTP_REFERER']
    p = url.split("lists")

    if "details" in p[1]:
        p = p[1].split("/")
        if "page" in p[4]:
            n = p[4].split('=')[1]
        else:
            n = 1
        add_dict = {'type': p[2], 'ran': [p[3],p[4].split("?")[0]],'page': n}
        dict_ret.update(add_dict)
    return render(request,'lists/index.html',dict_ret,context)


def item_view(request,type,ran1,ran2):
    context = RequestContext(request)
    if type == "Epee":
        ret = 'Épée'
    elif type == "Sac":
        ret = 'Sac à dos'
    elif type == "Baton":
        ret = "Bâton"
    elif type == "Trophee":
        ret = "Trophée"
    else:
        ret = type
    ran = [ran1,ran2]
    return render(request,'lists/index.html',{'type': ret, 'ran': ran},context)

@login_required
def add_item(request,list_id,item_id):
    context = RequestContext(request)
    item = ListItem()
    listObj = List.objects.get(pk=list_id)
    itemObj = Objet.objects.get(ID=item_id)
    item.ID = listObj
    item.itemID = itemObj
    item.save()
    dict_ret = {'added': True}
    url =  request.META['HTTP_REFERER']
    p = url.split("lists")
    print p
    if "details" in p[1]:
        p = p[1].split("/")
        if "page" in p[4]:
            n = p[4].split('=')[1]
        else:
            n = 1
        add_dict = {'type': p[2], 'ran': [p[3],p[4].split("?")[0]],'page': n}
        dict_ret.update(add_dict)
    return render(request,'lists/index.html',dict_ret,context)

def list_view(request,list_id):


    return render(request,'lists/index.html',dict_ret,context)
