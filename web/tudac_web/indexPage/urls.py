from django.urls import path
from . import views

app_name="indexPage"
urlpatterns = [
    path('',views.index,name='index'),
    path('sermons/',views.sermons,name='sermon'),
    path('about/',views.about,name='views'),
    path('contact/',views.contact,name='contact'),
    path('events/',views.events,name='events'),

    path('mapChange/',views.mapChange,name='mapChange'),
    path('boringChange/',views.boringChange,name="boringChange"),
    path('time/',views.time,name="time"),
]