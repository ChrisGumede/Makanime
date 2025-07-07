from django.shortcuts import render
from .models import AnimeCatalog
from .models import models
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    catalog = AnimeCatalog.objects.all()

    #search funtionality
    anime_name = request.GET.get('anime_name')
    if anime_name != '' and anime_name is not None:
        catalog = catalog.filter(title__icontains=anime_name)
    
    #creat paginator instances
    paginator = Paginator(catalog,2)
    page = request.GET.get('page')
    catalog = paginator.get_page(page)

    return render(request,'Anime/index.html',{'catalog':catalog})

def detail(request,id):
    catalog = AnimeCatalog.objects.get(id=id) 
    return render(request,'anime/detail.html',{'catalog':catalog })