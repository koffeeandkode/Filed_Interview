from django.urls import path
from django.conf.urls import url 

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    
    url(r'^audio_server_webApp/create/', views.create_api),
    url(r'^audio_server_webApp/delete/(?P<audioFileType>[\w-]+)/(?P<audioFileID>\d+)/', views.delete_api),
    url(r'^audio_server_webApp/update/(?P<audioFileType>[\w-]+)/(?P<audioFileID>\d+)/', views.update_api),
    url(r'^audio_server_webApp/get/(?P<audioFileType>[\w-]+)/(?P<audioFileID>\d+)/', views.get_api),
    url(r'^audio_server_webApp/get/(?P<audioFileType>[\w-]+)/$', views.get_api),
    

] 

