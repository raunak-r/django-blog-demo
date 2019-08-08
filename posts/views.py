# from urllib import quote_plus
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .forms import PostForm
from .models import Post


def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404

	if not request.user.is_authenticated():
		raise Http404

	form = PostForm(request.POST or None, request.FILES or None)
	# if request.method == 'POST':
	# 	print(request.POST)
	# 	print(form.cleaned_data.get('title'))
	
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Not Created")

	context = {
		"form" : form,
	}
	return render(request, "post_form.html", context)

def post_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404

	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance = instance)
	
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		'title' : instance.title,
		'instance' : instance,
		'form' : form,
	}

	return render(request, "post_form.html", context)

def post_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404

	instance = get_object_or_404(Post, slug=slug)
	instance.delete()

	messages.success(request, "Successfully Deleted")
	return redirect("posts:list")

def post_detail(request, slug=None):
	# This returns an error if not found.
	# instance = Post.objects.get(id = 3)

	# Only 2 posts exist. This will return a 404 not found page.
	instance = get_object_or_404(Post, slug=slug)
	if instance.draft or instance.publish > timezone.now().date():
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404

	# share_string = quote_plus(instance.content)

	context = {
		'title' : instance.title,
		'instance' : instance,
		# 'share_string': share_string,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	queryset = Post.objects.active()
	if request.user.is_staff or request.user.is_superuser:
		queryset = Post.objects.all()

	query = request.GET.get("query")
	if query:
		queryset = queryset.filter(title__icontains=query)

	paginator = Paginator(queryset, 3) # Show n contacts per page
	page_request_var = 'page'
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	context = {
		'object_list' : queryset,
		'title' : "List",
		'page_request_var' : page_request_var
	}
	
	return render(request, "post_list.html", context)
