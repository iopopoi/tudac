from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .models import Map_DB
import random
import time

def index(request):
    return render(request,'indexPage/index.html')

def sermons(request):
    return render(request,'indexPage/sermons.html')

def contact(request):
    return render(request,'indexPage/contact.html')

def events(request):
    return render(request, 'indexPage/events.html')

def about(request):    
    return render(request, 'indexPage/about.html')


# test, after delete

def test(request):
    return render(request, 'indexPage/Test.html')

@require_POST
def mapChange(request):
    index = random.randrange(1,Map_DB.objects.count()+1)
    liste = Map_DB.objects.get(pk=index)
    print(liste.theme)
    context = {'Region':liste.region, 'Name':liste.name.replace('#',' '), 'Lat':float(str(liste.latitude)), 'Lng':float(str(liste.longitude)), 'Zoom':17}
    print(index,context["Region"],context["Name"],context["Lat"],context["Lng"])
    return HttpResponse(json.dumps(context), content_type="application/json")

@require_POST
def timeChange(request):
    now = time.time()
    now += random.randrange(2500000,43720001)
    now = time.localtime(now)
    wday = ["월","화","수","목","금","토","일"]
    year = str(now.tm_year); month=str(now.tm_mon); day=str(now.tm_mday)
    if(len(year)==1): year="0"+year
    if(len(month)==1): month="0"+month
    if(len(day)==1): day="0"+day
    context={'Year':year,"Month":month,"Day":day,"Wday":wday[now.tm_wday]}
    print(context)
    return HttpResponse(json.dumps(context), content_type="application/json")