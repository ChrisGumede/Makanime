from django.urls import path
from . import views

app_name = 'anime'
urlpatterns = [
    path('anime/',views.index,name='index'),
    #funtion view for anime_list
    path('<int:id>/',views.detail,name='detail'),
    
]
