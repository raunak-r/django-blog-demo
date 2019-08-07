from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import PostForm
from .models import Post

# Create your views here.
def create(request):
	form = PostForm(request.POST or None)
	# if request.method == 'POST':
	# 	print(request.POST)
	# 	print(form.cleaned_data.get('title'))
	
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Created")
		# return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Not Created")

	context = {
		"form" : form,
	}
	return render(request, "post_form.html", context)

def update(request, pid=None):
	instance = get_object_or_404(Post, id = pid)
	form = PostForm(request.POST or None, instance = instance)
	
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		messages.success(request, "Successfully Updated")
		# return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		'title' : instance.title,
		'content' : instance.content,
		'form' : form,
	}

	return render(request, "post_form.html", context)

def delete(request, pid= None):
	instance = get_object_or_404(Post, id = pid)
	instance.delete()

	messages.success(request, "Post Deleted")
	return redirect("posts:list")

def detail(request, pid=None):
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