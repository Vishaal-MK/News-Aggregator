import requests
from bs4 import BeautifulSoup as BSoup
from django.shortcuts import render, redirect

from news.models import Headline
from news.forms import SearchForm

# Create your views here.


def scrape(request, name):
    Headline.objects.all().delete()
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = f"https://www.theonion.com/{name}"
    content = session.get(url).content
    soup = BSoup(content, "html.parser")

    News = soup.find_all("div", {"class": "sc-cw4lnv-12 kQoJyO"})

    for article in News:
        main = article.find_all("a", href=True)

        linkx = article.find("a", {"class": "sc-1out364-0 dPMosf js_link"})
        link = linkx["href"]

        titlex = article.find("h2", {"class": "sc-759qgu-0 cvZkKd sc-cw4lnv-6 jbPaGl"})
        title = titlex.text

        imgx = article.find("img")["data-src"]

        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = imgx
        new_headline.save()
    return redirect("../")


def news_list(request):
    query = request.GET.get('query', '')

    if query:
        headlines = Headline.objects.filter(title__icontains=query)
    else:
        headlines = Headline.objects.all()[::-1]
    context = {
        "object_list": headlines,
    }
    return render(request, "news/home.html", context)

def search(request):
    form = SearchForm()
    query = None
    results = []
    
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Headline.objects.filter(title__icontains=query)
    
    return render(request, 'news/search.html', {'form': form, 'query': query, 'results': results})