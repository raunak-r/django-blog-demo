from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post

# Create your views here.
def create(request):
	return render(request, "index.html", {})

def detail(request, pid):
	# This returns an error.
	# instance = Post.objects.get(id = 3)

	# Only 2 posts exist. This will return a 404 not found page.
	instance = get_object_or_404(Post, id = pid)

	context = {
		'title' : "Detail",
		'instance' : instance,
	}
	return render(request, "post_detail.html", context)

def listall(request):
	queryset = Post.objects.all()

	context = {
		'postList' : queryset,
		'title' : "List",
	}
	
	return render(request, "index.html", context)