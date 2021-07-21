from django.shortcuts import redirect, render
from googleapiclient.http import RequestMockBuilder
import tmdbsimple as tmdb
from decouple import config
from googleapiclient.discovery import build
import requests,json


# Create your views here.
def movies1(request,category):
    key =  config('API_KEY')  
    url =  config('url') 
    url2 = url.format(category,key)
    urll = requests.get(url2)
    urlll = urll.json()
    return urlll

def movies(request):
    popular = movies1(request,'popular')
    upcoming = movies1(request,'upcoming')
    latest = movies1(request,'latest')
    topRated = movies1(request,'top_rated')

    return render(request,'movies.html',{'popular':popular,"upcoming":upcoming,"latest":latest,"toprated":topRated})


def youtube(request,id):
    youtubeapikey =  config('youtubeapikey')
    popular = movies1(request,'popular')
    popularmovie = ''
    for movie in popular['results']:
        if str(movie['id'])==str(id):
            popularmovie = movie['title']
    youtube = build('youtube','v3',developerKey = youtubeapikey)
    req = youtube.search().list(q= popularmovie+'trailer',part = 'snippet',type= 'video')
    res = req.execute()
    return render(request,'youtube.html',{'response':res})



