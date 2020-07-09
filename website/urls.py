
from django.urls import path
from . import views

urlpatterns = [

	path('', views.index, name="index"),
	path('about.html', views.about, name="about"),
	path('contact.html', views.contact, name="contact"),
	path('main.html', views.main, name="main"),
	path('news.html', views.news, name="news"),
	path('search.html', views.search, name="search"),
	path('listing1.html', views.listing1, name="listing1"),
	path('listing2.html', views.listing2, name="listing2"),
	path('listing3.html', views.listing3, name="listing3"),
	path('listing4.html', views.listing4, name="listing4"),



	
]