from django.conf.urls import url, include

from .views import (create,
					update,
					delete,
					detail,
					listall)

urlpatterns = [
	url(r'^create/$', create, name="create"),
	url(r'^(?P<pid>\d+)/update/$', update, name="update"),
	url(r'^(?P<pid>\d+)/delete/$', delete, name="delete"),

	url(r'^(?P<pid>\d+)/$', detail, name="detail"),
	# http://localhost:8000/posts/detail/1/
	
	url(r'^$', listall, name="list"),
]