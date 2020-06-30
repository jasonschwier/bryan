
from django.urls import path
from . import views

urlpatterns = [
	path('home.html', views.home, name="home"),
	path('', views.index, name="index"),

	
]