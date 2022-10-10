from django.urls import path
from .views import MainPageView,  NewsDetailView, WorldNewsView, UzbNewsView

urlpatterns = [
    path('', MainPageView, name='home'),
    path('worldnews/', WorldNewsView, name='wnews'),
    path('uzbnews/', UzbNewsView, name='uzbnews'),
    path('detail/', NewsDetailView, name='detail'),
]
