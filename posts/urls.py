from django.conf.urls import url, include

from .views import post_home

urlpatterns = [
	url(r'^$', post_home),
]