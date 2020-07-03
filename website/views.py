from django.shortcuts import render


def index(request):
	return render(request, 'index.html', {})

def about(request):
	return render(request, 'about.html', {})

def contact(request):
	return render(request, 'contact.html', {})

def listing1(request):
	return render(request, 'listing1.html', {})

def main(request):
	return render(request, 'main.html', {})

def news(request):
	return render(request, 'news.html', {})

def search(request):
	return render(request, 'search.html', {})



