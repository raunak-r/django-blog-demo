from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create(request):
	return render(request, "index.html", {})

def detail(request):
	context = {
		'title' : "Detail"
	}
	return render(request, "index.html", context)

def listall(request):
	context = {
		'title' : "List"
	}
	return render(request, "index.html", context)