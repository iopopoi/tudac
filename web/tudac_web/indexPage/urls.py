from django.urls import path
from . import views

app_name="indexPage"
urlpatterns = [
    path('',views.index,name='index'),
    path('sermons/',views.sermons,name='sermon'),
    path('about/',views.about,name='views'),
    path('contact/',views.contact,name='contact'),
    path('events/',views.events,name='events'),

    #test, after delete
    path('test/',views.test, name="test"),
    path('mapChange/',views.mapChange,name='mapChange'),
    path('timeChange/',views.timeChange,name="timeChange"),
    path('boringChange/',views.boringChange,name="boringChange")
]