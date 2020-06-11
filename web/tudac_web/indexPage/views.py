from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


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
def test(request, *args, **kwargs):
    if(kwargs['x']==0):
        kwargs = {'Lat':36.515694,'Lng':127.877974,'Zoom':6}
    else:
        kwargs = {'Lat':36.515694,'Lng':127.877974,'Zoom':7}

    return render(request, 'indexPage/JungTest.html', {'Lat':kwargs['Lat'],'Lng':kwargs['Lng'],'Zoom':kwargs['Zoom']})