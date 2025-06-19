from django.urls import path
from . import views

app_name = 'anime'
urlpatterns = [
    path('anime/',views.Anime_List,name='Anime_List'),
    #funtion view for anime_list
    
]
