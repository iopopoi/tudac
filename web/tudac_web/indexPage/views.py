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

#def index~about: 각 페이지를 render
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


#mapChange: 웹(어디가 페이지)에 맵 데이터베이스에서 랜덤으로 추출한 지역, 위치, 이미지, 위도경도를 전해줌
@require_POST
def mapChange(request):
    index = random.randrange(1,Map_DB.objects.count()+1) # 맵 DB의 id중 하나 랜덤 추출
    liste = Map_DB.objects.get(pk=index) # 해당 id의 db정보 가져옴

    #가져온 db를 토대로 전달해줄 contexdt 작성
    context = {'Region':liste.region, 'Name':liste.name.replace('#',' '), 'Image':liste.theme,'Lat':float(str(liste.latitude)), 'Lng':float(str(liste.longitude)), 'Zoom':17}
    print(context)

    #json형식으로 바꿔서 전달
    return HttpResponse(json.dumps(context), content_type="application/json")


#time: 웹(언제가 페이지)에 오늘 날짜를 기준으로 캘린더를 작성하기 위한 정보를 만들어서 전달하거나, 랜덤한 날짜를 기준으로 캘린더를 작성하기 위한 정보 전달
@require_POST
def time(request):

    # year와 month를 받고, 그 달의 날 수를 반환
    def maxday(year, month):
        if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12): return 31
        if(month==4 or month==6 or month==9 or month==11): return 30
        if((year%4==0)and(year%100!=0) or year%400==0): return 29
        else: return 28

    # year과 month를 받고, 전 달의 년도, 달 반환
    def before(year,month):
        month -= 1
        if month==0:
            year-=1;month=12
        return year,month 

    # year, month, day를 받고 정상적인 연월일로 바꿔줌 (2020,13,35) -> (2021,2,4)
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

    #만약에 처음 호출된거면(아닐수도있지만, 밑에서 예외처리) 오늘의 연월일,  시간은 한국기준(utc+9)
    now_day = datetime.datetime.utcnow()+datetime.timedelta(hours=9)
    year = now_day.year
    month = now_day.month
    day = now_day.day

    #만약에 처음 호출된게 아니라고 하면 랜덤한 연월일로
    if(request.POST['first'] == "false"):
        year = random.randrange(year,year+30)
        month = month+random.randrange(1,12)
        day = day+random.randrange(1,31)
    year,month,day = defini(year,month,day)

    #year, month, day로 datetime객체 생성
    today = datetime.date(year,month,day)

    #캘린더 리스트 틀 생성
    calender = [[],[],[],[],[]]
    for i in range(5): 
        for j in range(7): calender[i].append(0)

    # 캘린더에 이번 달, 다음 달 day 적기
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
