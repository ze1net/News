from django.shortcuts import render
from .models import NewsModel
from django.db.models import Q
from django.http import  HttpResponseRedirect

def MainPageView(request):
    news = NewsModel.objects.all()
    search = request.GET.get('q', '')
    if search:
        news = news.filter(Q(body__icontains=search) | Q(title__icontains=search) | Q(category__icontains=search))
        return render(request, 'pages/main_page.html', context={
            'news': news
        })
    return render(request, 'pages/main_page.html', context={
        'news': news
    })



def WorldNewsView(request):
    news = NewsModel.objects.all()
    return render(request, 'pages/worldnews_page.html', context={
        'news': news
    })
def UzbNewsView(request):
    news = NewsModel.objects.all()
    return render(request, 'pages/uzbnews_page.html', context={
        'news': news
    })
def NewsDetailView(request):
    new = NewsModel.objects.get()
    return render(request, 'pages/news_detail.html', context={
        'new': new
    })