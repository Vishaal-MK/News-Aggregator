from django.urls import path
from news.views import scrape, news_list, search
urlpatterns = [
  path('scrape/<str:name>', scrape, name="scrape"),
  path('search/', search, name="search"),
  path('', news_list, name="home"),
]