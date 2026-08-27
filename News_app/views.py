from django.shortcuts import render
from .models import news
from django.core.paginator import Paginator
# Create your views here.

def index_page(request):
    new = news.objects.all()
    paginator = Paginator(new , 6)

    page_num = request.GET.get("page")

    new = paginator.get_page(page_num)

    contact = {
        "news" : new
        }
    return render(request , "news/news.html" , contact)

def single_page(request , pid):
    the_new = news.objects.filter(id = pid)
    contact = {"news": the_new}
    return render(request , "news/single-news.html" , contact)