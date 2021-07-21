from django.conf.urls import url
from . import views


urlpatterns = [
      url(r'^$',views.movies,name='index'),
      url(r'^youtube/(\d+)',views.youtube,name = 'netflix'),
]