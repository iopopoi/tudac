from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('sermons/',views.sermons,name='sermon'),
    path('about/',views.about,name='views'),
    path('contact/',views.contact,name='contact'),
    path('events/',views.events,name='events'),
]