from django.shortcuts import render
from .models import AnimeCatalog
from django.core.paginator import Paginator

# Create your views here.
def Anime_List(request):
    anime_objects = AnimeCatalog.objects.all()

    #search funtionality
    anime_name = request.GET.get('anime_name')
    if anime_name != '' and anime_name is not None:
        anime_objects = anime_objects.filter(title__icontains=anime_name)
    
    #creat paginator instances
    paginator = Paginator(anime_objects,2)
    page = request.GET.get('page')
    anime_objects = paginator.get_page(page)

    return render(request,'Anime/anime_list.html',{'anime_objects':anime_objects})