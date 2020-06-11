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
from indexPage.models import Map_DB
import sqlite3


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
    
    context = {'Lat':36, 'Lng':127, 'Zoom':13}
    return HttpResponse(json.dumps(context), content_type="application/json")