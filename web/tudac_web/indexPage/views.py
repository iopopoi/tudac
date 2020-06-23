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
from .models import Boring_DB
import random
import time, datetime
import json

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
    context = {'Region':liste.region, 'Name':liste.name.replace('#',' '), 'Lat':float(str(liste.latitude)), 'Lng':float(str(liste.longitude)), 'Zoom':17}
    print(index,context["Region"],context["Name"],context["Lat"],context["Lng"])
    return HttpResponse(json.dumps(context), content_type="application/json")


@require_POST
def time(request):
    def maxday(year, month):
        if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12): return 31
        if(month==4 or month==6 or month==9 or month==11): return 30
        if((year%4==0)and(year%100!=0) or year%400==0): return 29
        else: return 28
    def before(year,month):
        month -= 1
        if month==0:
            year-=1;month=12
        return year,month 
    def defini(year,month,day):
        while(month>12):
            month = month-12
            year += 1
        while(day>maxday(year,month)):
            day -= maxday(year,month)
            month += 1
            if(month>12):
                year +=1
                month=1
        return year,month,day

    now_day = datetime.datetime.utcnow()+datetime.timedelta(hours=9)
    year = now_day.year
    month = now_day.month
    day = now_day.day
    if(request.POST['first'] == "false"):
        print("this!\n\n\n\n\n")
        year = random.randrange(year,year+30)
        month = month+random.randrange(1,12)
        day = day+random.randrange(1,31)
    year,month,day = defini(year,month,day)
    today = datetime.date(year,month,day)
    calender = [[],[],[],[],[]]
    for i in range(5): 
        for j in range(7): calender[i].append(0)

    firstday = datetime.date(today.year,today.month,1)
    firstwd = (firstday.weekday()+1)%7
    x_position=0; y_position=0
    now=1;x=firstwd; y=0; maxd = maxday(firstday.year,firstday.month)
    while(y<5):
        calender[y][x]=str(now)
        if(now==today.day):
            x_position=x 
            y_position=y
        now+=1
        if(int(calender[y][x])>maxd):
            calender[y][x]=str(int(calender[y][x])%maxd)
        x+=1
        if(x==7):
            x=0; y+=1
    x=firstwd-1;now=0;by,bm=before(firstday.year,firstday.month)
    while(x>=0):
        calender[0][x]=str(maxday(by,bm)+now)
        x-=1;now-=1
    
    for i in range(5):
        for j in range(7):
            if(len(calender[i][j])==1): calender[i][j] = "0"+calender[i][j]
    wday = ["Mon","Thes","Wednes","Thurs","Fri","Satur","Sun"]
    context = {'tyear':today.year, 'tmonth':today.month, 'tday':today.day, 'wday':wday[today.weekday()], 'xposition':x_position, 'yposition':y_position, 'calender':calender}
    print(context)
    return HttpResponse(json.dumps(context), content_type="application/json")


@require_POST
@csrf_exempt
def boringChange(request):
    array=request.POST['name'].split(',')[:-1]
    while("" in array):
        array.remove("")
    if(not array):
        context={'isempty':True, 'name':None,'do':None}
        return HttpResponse(json.dumps(context), content_type="application/json")

    index = random.randrange(1,Boring_DB.objects.count()+1)
    context={'isempty':False, 'name':random.choice(array),'do':Boring_DB.objects.get(pk=index).todo}
    return HttpResponse(json.dumps(context), content_type="application/json")
