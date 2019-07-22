from django.conf.urls import url, include

from .views import (create,
					detail,
					listall)

urlpatterns = [
	url(r'^create/', create),

	url(r'^(?P<pid>\d+)/$', detail, name = "detail"),
	# http://localhost:8000/posts/detail/1/
	
	url(r'^listall', listall),
]