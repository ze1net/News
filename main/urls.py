from django.urls import path
from .views import MainPageView,  NewsSearchView, WorldNewsView, UzbNewsView

urlpatterns = [
    path('', MainPageView, name='home'),
    path('search/', NewsSearchView, name='search'),
    path('worldnews/', WorldNewsView, name='wnews'),
    path('uzbnews/', UzbNewsView, name='uzbnews'),
]